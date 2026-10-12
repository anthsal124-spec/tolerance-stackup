import numpy as np
import pytest
import pandas as pd

from stackup import (
    calc_worst_case,
    calc_wc_contributions,
    calc_rss, calc_rss_contributions,
    simulate_gaps, calc_pct_out_of_spec
)


def housing_arrays():
    """Return the housing stack as four arrays."""

    nominals = np.array([50.00, 12.00, 15.50, 8.25, 13.75])
    plus_tols = np.array([0.10, 0.05, 0.05, 0.00, 0.08])
    minus_tols = np.array([0.10, 0.05, 0.05, 0.10, 0.08])
    directions = np.array([1, -1, -1, -1, -1])

    return nominals, plus_tols, minus_tols, directions


def test_worst_case_housing_stack():
    """Worst-case gap for the housing stack matches the hand calc: 0.22 to 0.88 mm."""
    nominals, plus_tols, minus_tols, directions = housing_arrays()

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
    nominals, plus_tols, minus_tols, directions = housing_arrays()

    min_gap, max_gap = calc_rss(nominals, plus_tols, minus_tols, directions)

    assert min_gap == pytest.approx(0.3954, abs=0.0001)
    assert max_gap == pytest.approx(0.7046, abs=0.0001)


def test_rss_contributions_housing_stack():
    """Housing contributions add to 100%, Housing contributes 41.84%, and the root-sum-square of half bands equal the RSS +/- range."""
    stack = pd.DataFrame({
        "name": ["Housing", "Part A", "Part B", "Spacer", "Part C"],
        "nominal": [50.00, 12.00, 15.50, 8.25, 13.75],
        "plus_tol": [0.10, 0.05, 0.05, 0.00, 0.08],
        "minus_tol": [0.10, 0.05, 0.05, 0.10, 0.08],
        "direction": [1, -1, -1, -1, -1],
    })

    contributions = calc_rss_contributions(stack)

    assert contributions["contribution_pct"].sum() == pytest.approx(100)
    assert contributions["name"].iloc[0] == "Housing"
    assert contributions["contribution_pct"].iloc[0] == pytest.approx(41.84, abs=0.01)

    nominals = stack["nominal"].to_numpy()
    plus_tols = stack["plus_tol"].to_numpy()
    minus_tols = stack["minus_tol"].to_numpy()
    directions = stack["direction"].to_numpy()

    min_gap, max_gap = calc_rss(nominals, plus_tols, minus_tols, directions)

    assert np.sqrt(np.sum(contributions["half_band"] ** 2)) == pytest.approx((max_gap - min_gap) / 2, abs=0.0001)
    assert "half_band" not in stack.columns


def test_pct_out_of_spec_simple():
    """Two of four values outside the limits gives 50%."""
    pct_out = calc_pct_out_of_spec(gaps=np.array([1.0, 2.0, 3.0, 4.0]), lower_limit=1.5, upper_limit=3.5)
    assert pct_out == pytest.approx(50)


def test_simulate_gaps_is_reproducible():
    """Two runs with the same seed are identical, a run with a different seed is not, and the array has exactly n_sample values."""
    nominals, plus_tols, minus_tols, directions = housing_arrays()
    gaps_1 = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=1_000, seed=50)
    gaps_2 = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=1_000, seed=50)
    gaps_3 = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=1_000, seed=51)

    assert len(gaps_1) == 1_000
    assert np.array_equal(gaps_1, gaps_2)
    assert not np.array_equal(gaps_1, gaps_3)


def test_simulate_gaps_matches_rss():
    """Default normal distribution, gaps' mean equals the RSS gap center and std dev equals RSS +/- / 3 within 2%."""
    nominals, plus_tols, minus_tols, directions = housing_arrays()
    gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions)
    mean = np.mean(gaps)

    min_gap, max_gap = calc_rss(nominals, plus_tols, minus_tols, directions)
    center = (min_gap + max_gap) / 2
    plus_minus = (max_gap - min_gap) / 2

    assert mean == pytest.approx(center, abs=0.001)

    std = np.std(gaps)

    assert std == pytest.approx(plus_minus/3, rel=0.02)


def test_simulate_gaps_rejects_unknown_distribution():
    """An unknown distribution name raises ValueError."""
    nominals, plus_tols, minus_tols, directions = housing_arrays()
    with pytest.raises(ValueError):
        simulate_gaps(nominals, plus_tols, minus_tols, directions, distribution="triangle")
