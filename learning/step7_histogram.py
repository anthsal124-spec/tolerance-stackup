import matplotlib.pyplot as plt
import pandas as pd
from stackup import simulate_gaps

# Load the CSV
df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

# Simulate 100,000 gaps with normal distribution
n_samples = 100_000

gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, n_samples=n_samples)

# Draw a histogram with 60 bins
fig, ax = plt.subplots(figsize=(8, 4.5))

ax.hist(gaps, bins=60, color="#2a78d6")

ax.set_xlabel("Gap (mm)")
ax.set_ylabel("Number of Assemblies")
ax.set_title(f"Simulated Gap, Housing Stack ({n_samples:,} Assemblies, Normal Parts)")

# Save
fig.savefig("plots/gap_histogram.png", dpi=150, bbox_inches="tight")
plt.show()
