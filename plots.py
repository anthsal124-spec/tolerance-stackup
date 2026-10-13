import matplotlib.pyplot as plt
from stackup import calc_pct_out_of_spec


def plot_gap_histogram(gaps, lower_limit, upper_limit, rss_limits, wc_limits, title):
    """Return a figure and axes showing the gap histogram with its limits marked."""

    min_gap_wc, max_gap_wc = wc_limits
    min_gap_rss, max_gap_rss = rss_limits

    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")

    ax.hist(gaps, bins=60, color="#2a78d6")

    ax.set_xlabel("Gap (mm)")
    ax.set_ylabel("Number of assemblies")

    # Draw 6 limits
    ax.axvline(lower_limit, color="#0b0b0b", linestyle="-", linewidth=1.5, label="Requirement limits")
    ax.axvline(upper_limit, color="#0b0b0b", linestyle="-", linewidth=1.5)

    ax.axvline(min_gap_rss, color="#eb6834", linestyle="--", linewidth=1.5, label="RSS range")
    ax.axvline(max_gap_rss, color="#eb6834", linestyle="--", linewidth=1.5)

    ax.axvline(min_gap_wc, color="#1baf7a", linestyle=":", linewidth=1.5, label="Worst-case range")
    ax.axvline(max_gap_wc, color="#1baf7a", linestyle=":", linewidth=1.5)

    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)

    # Report result
    pct_outside = calc_pct_out_of_spec(gaps, lower_limit, upper_limit)

    # Remove top and right edges, add second line to title
    ax.spines[["top", "right"]].set_visible(False)

    result = f"{pct_outside:.3f}% outside the {lower_limit:.2f} to {upper_limit:.2f} mm requirement"
    ax.set_title(f"{title}\n{result}")

    return fig, ax
