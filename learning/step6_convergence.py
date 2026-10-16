import pandas as pd
from stackup.core import calc_rss, simulate_gaps, calc_pct_out_of_spec

df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

min_gap_rss, max_gap_rss = calc_rss(nominals, plus_tols, minus_tols, directions)
print(f"RSS range: {min_gap_rss:.3f} to {max_gap_rss:.3f} mm")

print()

# Experiment 1: more samples
for n_samples in [100, 1_000, 10_000, 100_000, 1_000_000]:
    gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples)
    pct_out = calc_pct_out_of_spec(gaps, lower_limit=min_gap_rss, upper_limit=max_gap_rss)

    print(f"{n_samples:>10,} samples: {pct_out:.3f}% outside")

print()

# Experiment 2: different seeds
for n_samples in [1_000, 100_000]:
    for seed in [1, 2, 3, 4, 5]:
        gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples, seed=seed)
        pct_out = calc_pct_out_of_spec(gaps, lower_limit=min_gap_rss, upper_limit=max_gap_rss)

        print(f"{n_samples:>10,} samples, seed {seed}: {pct_out:.3f}% outside")

