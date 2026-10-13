import matplotlib.pyplot as plt
import pandas as pd
from stackup import simulate_gaps, calc_rss, calc_worst_case, calc_pct_out_of_spec

# Load the CSV
df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

# Simulate 100,000 gaps with normal distribution
n_samples = 100_000

gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples)

# Requirement
lower_limit = 0.35
upper_limit = 0.75

# Worst case limits
min_gap_wc, max_gap_wc = calc_worst_case(nominals, plus_tols, minus_tols, directions)

# RSS limits
min_gap_rss, max_gap_rss = calc_rss(nominals, plus_tols, minus_tols, directions)

# Draw a histogram with 60 bins
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

title = f"Simulated gap, housing stack ({n_samples:,} assemblies, normal parts)"
result = f"{pct_outside:.3f}% outside the {lower_limit:.2f} to {upper_limit:.2f} mm requirement"
ax.set_title(f"{title}\n{result}")

# Save
fig.savefig("plots/gap_histogram.png", dpi=150, bbox_inches="tight")
plt.show()
