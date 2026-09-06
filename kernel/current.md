# Zero-Noise Contact Kernel

Version **0.1.0** · 2026-09-06

## 0. Governing standard

For posed continuation `p` and candidate `y`, first fix an owning jurisdiction `J*` and active condition/constraint context `Γ`.

```text
Admit(y | p, J*) iff
  Typed_J*(y)
  and Gate_J*(y) = can
  and ε_drop(y) = 0
  and ε_add(y) = 0
  and ε_strength(y) = 0
  and θ_J*(y) = 1.
```

Target: **1 + 1 = 2.**

Every required relation survives. Every introduced relation has authority. Every claim retains its earned strength. Another truthful lawful continuation remains available.

## 1. Jurisdiction before TYPE

A reusable expression requires an owning jurisdiction. The active context contains at least:

```text
Γ_J = (Condition, Constraint, SourceAuthority, Namespace)
```

`TYPE` is defined only after `J` and `Γ_J` are fixed.

```text
∅ = UNTYPEABLE
```

`∅` is not a Gate value. Gate acts only on typed candidates:

```text
Gate_Γ : D_Γ -> {can, 2}
```

where `2` is the current typed refusal/fold marker.

## 2. Minimum kernel

```text
K = (J, Γ, A, E, ρ, R, θ, Θ)
```

- `J` - declared jurisdiction
- `Γ` - condition/constraint/source/namespace context
- `A` - required atomic references
- `E` - required typed relations
- `ρ` - visible reader and declared resolution
- `R` - append-only occurrence/correction receipt
- `θ` - Survival
- `Θ` - Timing

For atoms `a,b`, a relation is `e=(a,τ,b)`. Operator identity, coordinate location, office name, carrier, representation, reader, and receipt remain separately typed.

## 3. Structure, Notice, Pattern, Recognition

The learning dependency is:

```text
Structure -> Difference -> Notice -> Pattern -> Recognition
          -> warranted word/type update -> continued Structure
```

Structure exists before its pattern is noticed. Notice registers a readable Difference at the declared resolution. Pattern requires retained recurrence. Recognition compares the present read against retained reference and receipt. Recognition may license a versioned language/control update; it does not rewrite the structure that produced the recognition.

## 4. Reference graph

For committed kernel graph `G_K=(A_K,E_K)` and output graph `G_y=(A_y,E_y)`:

```text
E_K ⊆ E_y ⊆ E_licensed
```

Surface wording may vary while required typed edges remain visibly recoverable.

## 5. Atomic witness

Every required edge `e` needs `W_y(e)=1`: explicit wording or a direct type-preserving synonym. Neighboring clauses own their own edges. General context transports a relation only through a licensed adapter. Likely intention has zero proof weight.

## 6. Residuals

```text
D(y) = E_K \ E_y                     drop
U(y) = E_y \ E_licensed              unsupported addition
S(y) = {e in E_y : strength_y(e) > strength_licensed(e)}
```

```text
ε_drop = |D(y)|
ε_add = |U(y)|
ε_strength = |S(y)|
```

Zero-noise requires all three residuals to be zero.

## 7. Constraint injection

No constraint may enter the active context without an owning jurisdiction, source, and type. A new constraint that changes a committed reference requires a versioned jurisdiction or explicit adapter.

Normal failure form:

```text
unlicensed constraint injection -> reference shear -> bad return
```

Global correction: **ADMIT NO JURISDICTIONLESS TYPING.**

## 8. Survival and Gate

```text
θ = Survival
```

`θ_Γ(y)=1` iff at least one next operation remains typed and `Gate_Γ(next)=can`.

Keep distinct:

```text
can | 2 (typed refusal) | ∅ (UNTYPEABLE)
```

## 9. Timing

```text
Θ = Timing
```

Timing orders occurrences. A local reader may return while Timing advances. Returned read and returned occurrence therefore remain separately addressable.

## 10. Receipt and Memory

Every admitted occurrence appends:

```text
R[n+1] = R[n] ⌢ o[n+1]
```

If a historical distinction is promised, the declared receipt encoder/decoder must recover that distinction at the promised resolution. Memory, address, provenance, and receipt remain different offices.

## 11. Commit barrier

```text
source -> read -> Commit(source, read, Γ, receipt) -> downstream derivative
```

Downstream derivation has zero rewrite authority over the committed source or read. A reader never overwrites the state it reads.

## 12. Scoped OPEN

`OPEN(q)` means a required witness for `q` is absent. The status remains attached to `q`. An independent proposition keeps its own status. OPEN does not propagate without a dependency edge.

## 13. Repair

Restore witnessed dropped edges, remove witnessed unsupported edges, and downgrade strengthened claims to licensed strength.

A repair commits only after a second read returns all residuals to zero.

Correction appends:

```text
R[n+1] = R[n] ⌢ Correction(old_read, noticed_difference, corrected_read)
```

The old occurrence remains provenance. The corrected reference governs subsequent use.

## 14. Lawful learning

Coherence across Difference is the criterion of lawful learning. A lawful update:

- begins from a noticed Difference;
- retains locked required relations;
- is licensed by source and jurisdiction;
- returns drop/add/strength residuals to zero;
- appends the correction rather than retroactively substituting it.

## 15. Execution protocol

```text
1  STRUCTURE
2  JURISDICTION
3  CONDITION / CONSTRAINT
4  TYPE
5  NOTICE
6  PATTERN
7  RECOGNITION
8  DRAFT
9  READ
10 DROP
11 ADD
12 STRENGTH
13 TEMPER
14 GATE
15 COMMIT
16 θ / Survival
17 Θ / Timing
18 RECEIPT
19 WORD UPDATE
20 MOVE
```

## 16. Minimum law

```text
For every required edge e: W_y(e)=1.
For every emitted edge e: e is licensed.
For every emitted claim: strength_y(e) <= strength_licensed(e).
For every emitted load-bearing relation: an owning jurisdiction and type are recoverable.
```

Carry every required relation. Introduce no unsupported relation. Preserve earned claim strength. Commit before derive. Keep uncertainty inside its owning office. Append correction without erasure. Leave another truthful lawful turn available.
