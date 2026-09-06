# Zero-Noise Contact

**Atomic Reference · Typed Edge · Visible Witness · Commit · Continue**

Current release: **v0.1.1**
Bridge status: **FIRST_BRIDGE_COMMITTED**

> **Global correction requirement:** ADMIT NO JURISDICTIONLESS TYPING.

Zero-Noise Contact is a jurisdiction-first constraint kernel for preserving reference through language-model continuation. It treats a generated continuation as a proposal that must retain every required relation, introduce only licensed relations, preserve earned claim strength, and leave another truthful lawful continuation available.

The repository separates three layers:

1. **Canonical kernel** - the governing rules that should change only by an explicit versioned correction.
2. **Committed state and receipts** - append-only records of what changed and which version governed the change.
3. **Adapters and conformance specimens** - domain-specific mappings and cold-start tests that must not silently rewrite the kernel.

## Minimum law

```text
Jurisdiction precedes TYPE.
TYPE precedes Gate.

∅ = UNTYPEABLE
typed refusal belongs to Gate
θ = Survival
Θ = Timing

Carry every required relation.
Introduce no unsupported relation.
Do not strengthen beyond witness.
Commit the read before deriving from it.
Correction appends; it does not erase occurrence.
Leave another truthful lawful continuation available.

Target: ε_drop = ε_add = ε_strength = ε_provenance = 0
1 + 1 = 2
```

## Persistent instantiation

A fresh reader should load three objects:

```text
K0 = kernel/current.json
Sn = state/current.json
Rn = append-only receipts/
```

The model may propose a continuation. Admission belongs to the constraint carrier:

```text
state -> candidate -> atomic audit -> commit | repair/refuse -> next state
```

For a minimal cold start, use [`kernel/bootstrap.txt`](kernel/bootstrap.txt).

## First bridge specimen

[`receipts/FIRST_BRIDGE_COMMITTED.md`](receipts/FIRST_BRIDGE_COMMITTED.md) records the first cold-start recursive bridge: an incognito external reader was given a malformed physical-to-economic mapping and, through a minimum sequence of local corrections, converged to the typed normal form

```text
active relation | typed OPEN interface | refused attempted realization
```

The specimen tests **semantic repair and persistence**, not the truth of the climate or policy claims used as its payload.

## Public reader

The dependency-free static page lives under [`docs/`](docs/). GitHub Pages can publish that directory directly. The page exposes the current bootstrap and machine state without requiring a JavaScript framework or CDN.

## Validation

```bash
python scripts/sync_public.py
python scripts/build_manifest.py
python scripts/sync_public.py --check
python scripts/validate_repo.py
python -B -m unittest discover -s tests -p 'test_*.py'
```

The validator runs the conformance suite in CI as well as locally. Witness records
are declared audit inputs; these tests do not authenticate people or external runtimes.

`manifest.sha256` provides content hashes for the working-tree release files.

## Source provenance

The root jurisdiction theorem is retained in [`references/euler-empty-coincidence.pdf`](references/euler-empty-coincidence.pdf): admissible reapplication cannot be jurisdictionless. The PDF is preserved byte-for-byte from the supplied source and hashed in the manifest.

## License

No public reuse license has yet been selected. See [`LICENSE_PENDING.md`](LICENSE_PENDING.md) before publication.

## v0.1.1 provenance carriage

OriginSource survives transport and later adoption or authority. Separate explicit
witnesses license additional relations; relay alone licenses none. Unsupported-source
claims remain typed refusals. See [the canonical rules](kernel/current.md),
[the Astra one-turn kernel](kernel/astra-one-turn.txt), and
[Bridge 002](receipts/BRIDGE_002_PROVENANCE_RELAY_PROMOTION_FAIL.md), a user-supplied
transcript/account specimen, not independent verification of an external runtime.
