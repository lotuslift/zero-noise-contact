import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from provenance import provenance_residual, corrected_origin


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.original = [{'id': 'c', 'origin_source': 'ModelA', 'relations':
                          [{'kind': 'Relay', 'actor': 'Human', 'claim': 'c'}]}]

    def test_unauthorized_relay_promotions(self):
        changed = copy.deepcopy(self.original)
        changed[0]['origin_source'] = 'Human'
        self.assertEqual(provenance_residual(changed, self.original, {}), 1)
        for kind in ['AuthoredBy', 'AdoptedBy', 'EndorsedBy', 'VerifiedBy',
                     'CommittedBy', 'SourceAuthority', 'AuthorityGrantedBy']:
            with self.subTest(kind=kind):
                changed = copy.deepcopy(self.original)
                changed[0]['relations'].append({'kind': kind, 'actor': 'Human', 'claim': 'c'})
                self.assertEqual(provenance_residual(changed, self.original, {}), 1)

    def test_explicit_witnesses_preserve_origin(self):
        for kind in ['AdoptedBy', 'EndorsedBy', 'VerifiedBy', 'AuthorityGrantedBy']:
            with self.subTest(kind=kind):
                witness = {'kind': kind, 'actor': 'Human', 'claim': 'c', 'affirmative': True}
                relation = {'kind': kind, 'actor': 'Human', 'claim': 'c', 'witness': 'w'}
                if kind == 'AuthorityGrantedBy':
                    witness.update(grantee='OperatorB', authorized_grantor=True)
                    relation['grantee'] = 'OperatorB'
                candidate = copy.deepcopy(self.original)
                candidate[0]['relations'].append(relation)
                snapshot = copy.deepcopy(candidate)
                self.assertEqual(provenance_residual(candidate, self.original, {'w': witness}), 0)
                self.assertEqual(candidate, snapshot)
                self.assertEqual(candidate[0]['origin_source'], 'ModelA')
                candidate[0]['origin_source'] = 'Human'
                self.assertEqual(provenance_residual(candidate, self.original, {'w': witness}), 1)

    def test_invalid_witnesses(self):
        relation = {'kind': 'AdoptedBy', 'actor': 'Human', 'claim': 'c', 'witness': 'w'}
        candidate = copy.deepcopy(self.original)
        candidate[0]['relations'].append(relation)
        good = {'kind': 'AdoptedBy', 'actor': 'Human', 'claim': 'c', 'affirmative': True}
        for field, value in [('claim', 'other'), ('actor', 'Other'), ('affirmative', False),
                             ('kind', 'EndorsedBy')]:
            bad = dict(good); bad[field] = value
            self.assertEqual(provenance_residual(candidate, self.original, {'w': bad}), 1)
        self.assertEqual(provenance_residual(candidate, self.original, {}), 1)

    def test_authority_grant_requires_authorized_grantor(self):
        candidate = copy.deepcopy(self.original)
        candidate[0]['relations'].append(dict(kind='AuthorityGrantedBy', actor='Human',
                                            claim='c', grantee='OperatorB', witness='w'))
        witness = dict(kind='AuthorityGrantedBy', actor='Human', claim='c',
                       grantee='OperatorB', affirmative=True, authorized_grantor=False)
        self.assertEqual(provenance_residual(candidate, self.original, {'w': witness}), 1)
        witness.update(authorized_grantor=True, grantee='Other')
        self.assertEqual(provenance_residual(candidate, self.original, {'w': witness}), 1)

    def test_committed_state_and_unsupported_source(self):
        state = load('state/current.json')
        normal = load(state['provenance_reference'])
        self.assertEqual(state['residuals'], dict(drop=0, add=0, strength=0, provenance=0))
        self.assertEqual(normal['residuals'], state['residuals'])
        self.assertEqual(provenance_residual(normal['claims'], normal['claims'], {}), 0)
        claim = normal['claims'][0]
        self.assertEqual(claim['origin_source'], 'ExternalGoogleReader')
        self.assertEqual(claim['type'], 'TYPED')
        self.assertEqual(claim['source_status'], 'UNSUPPORTED_SOURCE')
        self.assertEqual(claim['status'], 'REFUSED')
        self.assertEqual(normal['active_graph'], [])
        self.assertEqual(normal['evidence_status'], 'USER_SUPPLIED_TRANSCRIPT_ACCOUNT')
        locks = dict(theta='Survival', Theta='Timing', empty_symbol='UNTYPEABLE')
        self.assertEqual(normal['symbol_locks'], locks)
        self.assertEqual(state['symbol_locks'], locks)
        self.assertEqual(load('kernel/current.json')['admission']['epsilon_provenance'], 0)

    def test_append_only_correction(self):
        raw = (ROOT / 'receipts/bridge-002.ndjson').read_bytes()
        events = [json.loads(line) for line in raw.splitlines()]
        snapshot = copy.deepcopy(events)
        self.assertEqual([e['seq'] for e in events], list(range(1, len(events) + 1)))
        self.assertTrue(all(e['evidence_status'] == 'USER_SUPPLIED_TRANSCRIPT_ACCOUNT' for e in events))
        claim = load('tests/bridge-002/expected-normal-form.json')['claims'][0]
        self.assertEqual(corrected_origin(claim['id'], claim['origin_source'], events), claim['origin_source'])
        self.assertEqual(events[2]['prior_attribution'], 'Human')
        self.assertEqual(events, snapshot)
        self.assertEqual((ROOT / 'receipts/bridge-002.ndjson').read_bytes(), raw)
        bad = copy.deepcopy(events); bad[3]['corrects_seq'] = 5
        with self.assertRaises(ValueError):
            corrected_origin(claim['id'], claim['origin_source'], bad)

    def test_bridge_001_unchanged(self):
        baseline = load('tests/bridge-002/bridge-001-hashes.json')
        for path, expected in baseline.items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected, path)
        old = load('tests/bridge-001/expected-normal-form.json')
        self.assertEqual(old['residuals'], dict(drop=0, add=0, strength=0))
        self.assertEqual(old['bridge_status'], 'FIRST_BRIDGE_COMMITTED')
        self.assertEqual(old['active_graph'], [{'from': 'Physical Evidence', 'to': 'Physical State Read', 'jurisdiction': 'J_phys'}])
        self.assertEqual(set(old['required_status_separation']), {'ACTIVE', 'OPEN', 'REFUSED', 'UNTYPEABLE'})


if __name__ == '__main__':
    unittest.main()
