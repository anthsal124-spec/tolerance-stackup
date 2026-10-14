import matplotlib.pyplot as plt
import numpy as np
from stackup import calc_pct_out_of_spec


def plot_gap_histogram(gaps, lower_limit, upper_limit, rss_limits, wc_limits, title, ax=None, show_legend=True):
    """Return a figure and axes showing the gap histogram with its limits marked."""

    min_gap_wc, max_gap_wc = wc_limits
    min_gap_rss, max_gap_rss = rss_limits

    if ax is None:
        fig, ax = plt.subplots(figsize=(8,4.5), layout="constrained")
    else:
        fig = ax.figure

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

    if show_legend:
        ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)

    # Report result
    pct_outside = calc_pct_out_of_spec(gaps, lower_limit, upper_limit)

    # Remove top and right edges, add second line to title
    ax.spines[["top", "right"]].set_visible(False)

    result = f"{pct_outside:.3f}% outside the {lower_limit:.2f} to {upper_limit:.2f} mm requirement"
    ax.set_title(f"{title}\n{result}")

    return fig, ax


def plot_contributions(contributions, title):
    """Return a figure and axes showing contribution percentage."""

    positions = np.arange(len(contributions["name"]))
    bar_height = 0.38

    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")

    bars_wc = ax.barh(positions - bar_height / 2,
                      contributions["contribution_pct_wc"],
                      height=bar_height,
                      color="#1baf7a",
                      label="Worst-case")
    bars_rss = ax.barh(positions + bar_height / 2,
                       contributions["contribution_pct_rss"],
                       height=bar_height,
                       color="#eb6834",
                       label="RSS")

    ax.set_yticks(positions, labels=contributions["name"])
    ax.invert_yaxis()                            # put the first item at the top
    ax.bar_label(bars_wc, fmt="%.1f%%", padding=3)
    ax.bar_label(bars_rss, fmt="%.1f%%", padding=3)
    ax.legend(frameon=False)

    ax.set_xlabel("Contribution to gap variation (%)")
    ax.set_title(title)
    ax.margins(x=0.1)

    ax.spines[["top", "right"]].set_visible(False)

    return fig, ax


def plot_gap_comparison(gaps_normal, gaps_uniform, lower_limit, upper_limit, rss_limits, wc_limits, title):
    """Return a figure with normal and uniform gap histograms on shared axes."""
    fig, axes = plt.subplots(2, 1, sharex=True, sharey=True, figsize=(8, 9), layout="constrained")

    plot_gap_histogram(gaps_normal, lower_limit, upper_limit, rss_limits, wc_limits,
                       "Normal parts", ax=axes[0])     # top plot
    plot_gap_histogram(gaps_uniform, lower_limit, upper_limit, rss_limits, wc_limits,
                       "Uniform parts", ax=axes[1], show_legend=False)      # bottom plot
    axes[0].set_xlabel("")
    fig.suptitle(title)

    return fig, axes
