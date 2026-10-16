import matplotlib.pyplot as plt
import pandas as pd
from stackup.core import simulate_gaps, calc_rss, calc_worst_case
from stackup.plots import plot_gap_comparison

# Load the CSV
df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

# Simulate 100,000 gaps with normal distribution
n_samples = 100_000

gaps_normal = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples)
gaps_uniform = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples, distribution="uniform")

# Requirement
lower_limit = 0.35
upper_limit = 0.75

# Worst case limits
wc_limits = calc_worst_case(nominals, plus_tols, minus_tols, directions)

# RSS limits
rss_limits = calc_rss(nominals, plus_tols, minus_tols, directions)

# titles
title = f"Simulated gap, housing stack ({n_samples:,} assemblies)"

# create shared
fig, axes = plot_gap_comparison(gaps_normal, gaps_uniform, lower_limit, upper_limit, rss_limits, wc_limits, title)

# Save
fig.savefig("plots/gap_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
