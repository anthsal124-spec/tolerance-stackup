import numpy as np


def calc_worst_case(nominals, plus_tols, minus_tols, directions):
    """Return the worst-case minimum and maximum gap of a stack."""
    upper_limits = nominals + plus_tols
    lower_limits = nominals - minus_tols

    # Max gap: dimensions that open the gap at their upper limit,
    # dimensions that close it at their lower limit.
    max_case = np.where(directions > 0, upper_limits, lower_limits)
    max_gap = np.sum(max_case * directions)

    # Min gap: the reverse.
    min_case = np.where(directions > 0, lower_limits, upper_limits)
    min_gap = np.sum(min_case * directions)

    return min_gap, max_gap


def calc_wc_contributions(stack):
    """Return each dimension's worst-case tolerance band and % contribution, largest first."""
    result = stack.copy()
    result["tol_band"] = result["plus_tol"] + result["minus_tol"]
    result["contribution_pct"] = result["tol_band"] / result["tol_band"].sum() * 100
    result = result[["name", "tol_band", "contribution_pct"]]
    sorted_result = result.sort_values("contribution_pct", ascending=False)
    return sorted_result


def calc_rss(nominals, plus_tols, minus_tols, directions):
    """Return the RSS minimum and maximum gap of a stack.

    Assumes each dimension is normal, centered in its tolerance zone,
    independent of the others, with tolerance = +/-3 sigma.
    """
    center = nominals + (plus_tols - minus_tols) / 2
    half_band = (plus_tols + minus_tols) / 2
    gap_center = np.sum(directions * center)
    rss_plus_minus = np.sqrt(np.sum(half_band ** 2))
    min_gap = gap_center - rss_plus_minus
    max_gap = gap_center + rss_plus_minus

    return min_gap, max_gap

