import numpy as np
import pytest

from stackup import calc_worst_case


def test_worst_case_housing_stack():
    """Worst-case gap for the housing stack matches the hand calc: 0.22 to 0.88 mm."""
    nominals = np.array([50.00, 12.00, 15.50, 8.25, 13.75])
    plus_tols = np.array([0.10, 0.05, 0.05, 0.00, 0.08])
    minus_tols = np.array([0.10, 0.05, 0.05, 0.10, 0.08])
    directions = np.array([1, -1, -1, -1, -1])

    min_gap, max_gap = calc_worst_case(nominals, plus_tols, minus_tols, directions)

    assert min_gap == pytest.approx(0.22)
    assert max_gap == pytest.approx(0.88)


def test_worst_case_slot_stack():
    """Worst-case gap for the slot stack matches the hand calc: 0.1 to 0.3 mm."""
    nominals = np.array([30.00, 10.00, 19.80])
    plus_tols = np.array([0.05, 0.02, 0.03])
    minus_tols = np.array([0.05, 0.02, 0.03])
    directions = np.array([1, -1, -1])

    min_gap, max_gap = calc_worst_case(nominals, plus_tols, minus_tols, directions)

    assert min_gap == pytest.approx(0.1)
    assert max_gap == pytest.approx(0.3)
