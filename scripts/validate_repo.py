#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
errors=[]

def loadj(rel):
    try:
        return json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{rel}: {e}')
        return {}

version=(ROOT/'VERSION').read_text().strip()
k=loadj('kernel/current.json')
s=loadj('state/current.json')
e=loadj('tests/bridge-001/expected-normal-form.json')

if k.get('version') != version: errors.append('kernel version != VERSION')
if s.get('kernel_version') != version: errors.append('state kernel_version != VERSION')
if k.get('global_constraint') != 'ADMIT NO JURISDICTIONLESS TYPING': errors.append('global constraint drift')
ns=k.get('namespace',{})
if ns.get('empty_symbol_type') != 'UNTYPEABLE': errors.append('∅ lock drift')
if ns.get('theta') != 'Survival': errors.append('theta lock drift')
if ns.get('Theta') != 'Timing': errors.append('Theta lock drift')
if e.get('bridge_status') != 'FIRST_BRIDGE_COMMITTED': errors.append('bridge expected status drift')
if e.get('residuals') != {'drop':0,'add':0,'strength':0}: errors.append('bridge residual drift')
if set(e.get('open_registry',[])) != {'B_1->2','B_2->3','B_3->4'}: errors.append('bridge OPEN registry drift')

# Public mirrors must be byte-identical.
for a,b in [('kernel/bootstrap.txt','docs/canonical/bootstrap.txt'),('kernel/current.json','docs/canonical/current.json'),('state/current.json','docs/canonical/state.json')]:
    if (ROOT/a).read_bytes() != (ROOT/b).read_bytes(): errors.append(f'public mirror mismatch: {a} / {b}')

# Manifest validation.
manifest = ROOT/'manifest.sha256'
if not manifest.exists():
    errors.append('manifest.sha256 missing')
else:
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        expected, rel = line.split('  ',1)
        p=ROOT/rel
        if not p.is_file():
            errors.append(f'manifest missing file: {rel}')
            continue
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != expected: errors.append(f'hash mismatch: {rel}')

if errors:
    print('VALIDATION FAILED')
    for x in errors: print(' -',x)
    raise SystemExit(1)
print('VALIDATION PASSED')
print(f'kernel={version} bridge={e.get("bridge_status")} residuals=0/0/0')
