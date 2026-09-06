"""Conformance audit of declared claim relations, not authentication of humans.

The owning jurisdiction supplies trusted witness records. Candidate assertions
cannot authenticate their own witnesses. Audit never mutates either input.
"""

WITNESSED = {'AdoptedBy', 'EndorsedBy', 'VerifiedBy', 'AuthorityGrantedBy'}


def provenance_residual(candidate, retained, witnesses):
    """Count affected claim identities once, even with multiple failed relations."""
    reference = {c['id']: c for c in retained}
    failed = set()
    for claim in candidate:
        cid = claim['id']
        source = reference.get(cid)
        if source is None or claim.get('origin_source') != source['origin_source']:
            failed.add(cid)
        for relation in claim.get('relations', []):
            if source and relation in source.get('relations', []):
                continue
            kind = relation.get('kind')
            witness = witnesses.get(relation.get('witness'))
            valid = (kind in WITNESSED and witness is not None
                     and witness.get('affirmative') is True
                     and witness.get('claim') == cid == relation.get('claim')
                     and witness.get('actor') == relation.get('actor')
                     and bool(relation.get('actor'))
                     and witness.get('kind') == kind)
            if kind == 'AuthorityGrantedBy':
                valid = (valid and bool(relation.get('grantee'))
                         and witness.get('grantee') == relation.get('grantee')
                         and witness.get('authorized_grantor') is True)
            if not valid:
                failed.add(cid)
    return len(failed)


def corrected_origin(claim_id, retained_origin, history):
    """Resolve appended corrections for reuse without rewriting historical events."""
    origin = retained_origin
    by_seq = {event['seq']: event for event in history}
    for event in history:
        if event.get('event') != 'correction' or event.get('claim_id') != claim_id:
            continue
        prior = by_seq.get(event.get('corrects_seq'))
        if (prior is None or prior['seq'] >= event['seq']
                or prior.get('claim_id') != claim_id
                or event.get('prior_attribution') != prior.get('prior_attribution')
                or not event.get('noticed_provenance_difference')
                or event.get('corrected_attribution') != retained_origin):
            raise ValueError('Invalid attribution correction')
        origin = event['corrected_attribution']
    return origin
