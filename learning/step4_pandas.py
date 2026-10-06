import pandas as pd
from stackup import calc_worst_case

df = pd.read_csv("data/housing_stack.csv")
print(df)

df["upper"] = df["nominal"] + df["plus_tol"]
df["lower"] = df["nominal"] - df["minus_tol"]
print(df)

sorted_df = df.sort_values("nominal", ascending=False)
print(sorted_df)

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

min_gap, max_gap = calc_worst_case(nominals, plus_tols, minus_tols, directions)

print(f"Worst-case gap: {min_gap:.3f} to {max_gap:.3f} mm")
