import numpy as np
import pytest
import pandas as pd

from stackup import calc_worst_case, calc_wc_contributions, calc_rss


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


def test_wc_contributions_housing_stack():
    """Housing contributions add to 100%, Housing leads at 30.30%, and bands equal the worst-case range."""
    stack = pd.DataFrame({
        "name": ["Housing", "Part A", "Part B", "Spacer", "Part C"],
        "nominal": [50.00, 12.00, 15.50, 8.25, 13.75],
        "plus_tol": [0.10, 0.05, 0.05, 0.00, 0.08],
        "minus_tol": [0.10, 0.05, 0.05, 0.10, 0.08],
        "direction": [1, -1, -1, -1, -1],
    })

    contributions = calc_wc_contributions(stack)

    assert contributions["contribution_pct"].sum() == pytest.approx(100)
    assert contributions["name"].iloc[0] == "Housing"
    assert contributions["contribution_pct"].iloc[0] == pytest.approx(30.30, abs=0.01)

    nominals = stack["nominal"].to_numpy()
    plus_tols = stack["plus_tol"].to_numpy()
    minus_tols = stack["minus_tol"].to_numpy()
    directions = stack["direction"].to_numpy()

    min_gap, max_gap = calc_worst_case(nominals, plus_tols, minus_tols, directions)

    assert contributions["tol_band"].sum() == pytest.approx(max_gap - min_gap)
    assert "tol_band" not in stack.columns

def test_rss_housing_stack():
    """RSS gap for the housing stack matches the hand calc: 0.3954 to 0.7046 mm."""
    nominals = np.array([50.00, 12.00, 15.50, 8.25, 13.75])
    plus_tols = np.array([0.10, 0.05, 0.05, 0.00, 0.08])
    minus_tols = np.array([0.10, 0.05, 0.05, 0.10, 0.08])
    directions = np.array([1, -1, -1, -1, -1])

    min_gap, max_gap = calc_rss(nominals, plus_tols, minus_tols, directions)

    assert min_gap == pytest.approx(0.3954, abs=0.0001)
    assert max_gap == pytest.approx(0.7046, abs=0.0001)
