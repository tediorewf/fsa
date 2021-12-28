import unittest

from fsa.fsa import FiniteStateAutomata
from tests.mocks import fsa_non_det_mock1_params, fsa_det_mock1_params


class FiniteStateAutomataTestCase(unittest.TestCase):
    def test_should_determine_fsa_mock1_correctly(self) -> None:
        fsa_non_det = FiniteStateAutomata(**fsa_non_det_mock1_params)

        fsa_non_det.determine()

        self.assertEqual(fsa_det_mock1_params, fsa_non_det.to_dict())
