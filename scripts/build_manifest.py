#!/usr/bin/env python3
from pathlib import Path
import hashlib
from release_files import release_files

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

rows=[]
for rel in release_files(ROOT):
    p = ROOT / rel
    rows.append(f'{digest(p)}  {rel.as_posix()}')
text='\n'.join(rows)+'\n'
(ROOT/'manifest.sha256').write_text(text, encoding='utf-8', newline='\n')
(ROOT/'docs/canonical/manifest.sha256').write_text(text, encoding='utf-8', newline='\n')
print(f'Wrote {len(rows)} manifest entries')
