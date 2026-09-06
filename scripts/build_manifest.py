#!/usr/bin/env python3
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {Path('manifest.sha256'), Path('docs/canonical/manifest.sha256')}

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

rows=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '.git' in p.parts:
        continue
    rel = p.relative_to(ROOT)
    if rel in EXCLUDE:
        continue
    rows.append(f'{digest(p)}  {rel.as_posix()}')
text='\n'.join(rows)+'\n'
(ROOT/'manifest.sha256').write_text(text, encoding='utf-8')
(ROOT/'docs/canonical/manifest.sha256').write_text(text, encoding='utf-8')
print(f'Wrote {len(rows)} manifest entries')
