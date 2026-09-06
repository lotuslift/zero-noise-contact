#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys, re, subprocess
from release_files import release_files

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
if loadj('state/open-registry.json').get('kernel_version') != version: errors.append('OPEN registry version drift')
citation=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
if f'version: "{version}"' not in citation: errors.append('citation version drift')
page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
displayed=re.findall(r'\b\d+\.\d+\.\d+\b', page)
if not displayed or set(displayed) != {version}: errors.append('public page version drift')
for rel in ['README.md','kernel/current.md','kernel/bootstrap.txt','kernel/astra-one-turn.txt']:
    if version not in (ROOT/rel).read_text(encoding='utf-8'): errors.append(f'version missing: {rel}')
if 'ε_provenance = 0' not in page: errors.append('public page provenance missing')
if k.get('admission',{}).get('epsilon_provenance') != 0: errors.append('provenance admission drift')
if not k.get('provenance'): errors.append('provenance rules missing')
if s.get('residuals') != dict(drop=0,add=0,strength=0,provenance=0): errors.append('committed residual drift')
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
    listed=[]
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        if not re.fullmatch(r'[0-9a-f]{64}  .+', line):
            errors.append('malformed manifest line')
            continue
        expected, rel = line.split('  ',1)
        listed.append(rel)
        p=ROOT/rel
        if not p.resolve().is_relative_to(ROOT):
            errors.append(f'manifest path outside repository: {rel}')
            continue
        if not p.is_file():
            errors.append(f'manifest missing file: {rel}')
            continue
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != expected: errors.append(f'hash mismatch: {rel}')
    if len(listed) != len(set(listed)): errors.append('duplicate manifest entry')
    if set(listed) != {p.as_posix() for p in release_files(ROOT)}: errors.append('manifest release inventory mismatch')
    mirror=ROOT/'docs/canonical/manifest.sha256'
    if not mirror.exists() or manifest.read_bytes() != mirror.read_bytes(): errors.append('manifest mirror mismatch')

# Run the semantic conformance suite in local validation and CI.
result=subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py'], cwd=ROOT)
if result.returncode: errors.append('conformance tests failed')

if errors:
    print('VALIDATION FAILED')
    for x in errors: print(' -',x)
    raise SystemExit(1)
print('VALIDATION PASSED')
print(f'kernel={version} bridge={e.get("bridge_status")} current residuals=0/0/0/0; historical Bridge 001 unchanged')
