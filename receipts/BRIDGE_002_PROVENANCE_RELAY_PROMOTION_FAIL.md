# BRIDGE_002_PROVENANCE_RELAY_PROMOTION_FAIL

Evidence basis: **USER_SUPPLIED_TRANSCRIPT_ACCOUNT**

The human operator supplied a conversation transcript/account of an external
Google reader interaction. The following events are reported by that account;
the repository, Codex, GitHub, and OpenAI have not independently verified the
external runtime. No verbatim external transcript is reproduced here.

The account reports that an external Google reader generated unsupported
production/deployment claims, the human relayed that model output back to the
reader, and the reader promoted the relay into human/source authority.

The smallest failed relation is:

```text
(Human, transport, prior_model_output)
    does not imply
(Human, source, prior_model_output)
```

The account identifies the canonical baseline as v0.1.0 /
FIRST_BRIDGE_COMMITTED. Local inspection before this patch found that same
version/status at initial commit 8bd58eb1b272c69a90ad459305b10716596860c8.
The reported invented production history never became canonical repository
history. This receipt does not assert any deployment, production use, or that
Google wrote or committed anything to this repository.

Derived kernel result: Transport preserves originating source identity unless a
separately witnessed provenance relation licenses an additional authority relation.
OriginSource itself is never overwritten. Adoption, endorsement, verification,
and authority grants remain separate typed relations with explicit witnesses.

The failed generated production/deployment claims remain typed,
UNSUPPORTED_SOURCE / REFUSED historical occurrences, not ∅ / UNTYPEABLE.
Their exact wording is not supplied here and is not reconstructed.
They leave the active graph and remain in receipt provenance. Correction appends
the noticed attribution difference and corrected model origin; subsequent reuse
follows that correction without rewriting the failed historical attribution.

The companion bridge-002.ndjson encodes this supplied semantic structure.
Tests certify repository conformance to that structure, not the external event.
Independent external-runtime verification remains OPEN in its own evidence scope.
