# Publish the repository

This repository is already laid out for GitHub plus GitHub Pages.

## 1. Create the GitHub repository

Create an empty repository named, for example, `zero-noise-contact`.

From this working tree:

```bash
git remote add origin git@github.com:<owner>/zero-noise-contact.git
git push -u origin main
```

## 2. Enable GitHub Pages

In GitHub:

1. Open **Settings -> Pages**.
2. Choose **Deploy from a branch**.
3. Select branch `main` and folder `/docs`.
4. Save.

The public page will serve `docs/index.html`. The public machine-readable references are mirrored under `docs/canonical/` and validated against their authoritative repository counterparts.

## 3. Canonical and immutable references

Use two links in every external receipt:

- **moving canonical reference**: the current branch path, such as `kernel/bootstrap.txt`;
- **immutable reference**: the same file addressed by a Git commit SHA or release tag.

A future custom domain may point to the Pages site without changing the immutable Git history.

## 4. Before every release

```bash
python scripts/sync_public.py
python scripts/build_manifest.py
python scripts/sync_public.py --check
python scripts/validate_repo.py
git status
```

Then commit and tag:

```bash
git add .
git commit -m "Release ZNC v0.1.0"
git tag -a v0.1.0 -m "Zero-Noise Contact v0.1.0"
git push origin main --tags
```

## 5. Archival layer

After the repository is public and the author has selected a license, connect tagged releases to an archival service such as Zenodo if a DOI-backed citation layer is desired.

Do not publish until the license decision in `LICENSE_PENDING.md` has been resolved if public reuse terms matter.
