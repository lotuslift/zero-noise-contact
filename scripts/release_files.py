"""Shared release inventory; exclude only declared local/build artifacts."""
from pathlib import Path

MANIFESTS = {Path('manifest.sha256'), Path('docs/canonical/manifest.sha256')}


def release_files(root):
    return sorted(p.relative_to(root) for p in root.rglob('*')
                  if p.is_file()
                  and not set(p.relative_to(root).parts) & {'.git', '__pycache__', '_site'}
                  and p.suffix != '.pyc' and p.name != '.DS_Store'
                  and p.relative_to(root) not in MANIFESTS)
