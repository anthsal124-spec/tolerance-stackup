import pandas as pd
import numpy as np

from stackup.core import simulate_gaps, calc_rss, calc_worst_case

df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

n_samples = 100_000

# Simulate, call function
gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples)

# Statistics of simulated gaps
mean = np.mean(gaps)
standard_dev = np.std(gaps)

print(f"Mean gap: {mean:.4f} mm")
print(f"Standard deviation: {standard_dev:.4f} mm")

sample_min = np.min(gaps)
sample_max = np.max(gaps)

print(f"Min / max simulated: {sample_min:.4f} / {sample_max:.4f} mm")

# Limits to check against
min_gap_wc, max_gap_wc = calc_worst_case(nominals, plus_tols, minus_tols, directions)
min_gap_rss, max_gap_rss = calc_rss(nominals, plus_tols, minus_tols, directions)

# Percentage of gaps outside range
outside_wc = (gaps < min_gap_wc) | (gaps > max_gap_wc)
pct_outside_wc = np.mean(outside_wc) * 100

outside_rss = (gaps < min_gap_rss) | (gaps > max_gap_rss)
pct_outside_rss = np.mean(outside_rss) * 100

count_wc = np.sum(outside_wc)
count_rss = np.sum(outside_rss)
print(f"Outside worst case: {count_wc} of {n_samples} ({pct_outside_wc:.3f}%)")
print(f"Outside RSS: {count_rss} of {n_samples} ({pct_outside_rss:.3f}%)")
