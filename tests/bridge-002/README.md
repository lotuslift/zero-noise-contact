# Bridge 002 provenance conformance

Evidence basis: USER_SUPPLIED_TRANSCRIPT_ACCOUNT. The JSON normal form retains
the reported model origin and the human transport relation while refusing the
unsupported production/deployment claims. Zero provenance residual describes the
corrected reference; it does not validate the claims' substance or external events.

Run `python -B -m unittest discover -s tests -p 'test_*.py'`.
`scripts/validate_repo.py` invokes the same suite, including in the existing CI job.
Cases A–E cover unauthorized relay promotion, explicit adoption, explicit endorsement,
typed unsupported-source status, and append-only correction. Additional cases cover
verification, delegated authority, invalid witnesses, and locked committed state.

Witnesses are trusted inputs supplied by the owning jurisdiction, separate from
candidate output. The audit checks explicit actor/claim/relation matches, affirmative
intent, and declared grantor authorization. It does not authenticate identities or
decide whether a real-world person has authority. No runtime adoption is asserted.

bridge-001-hashes.json freezes the unmodified initial commit's Bridge 001 receipt
and fixture bytes. Historical three-residual records are not upgraded retroactively.
