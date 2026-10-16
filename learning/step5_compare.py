import pandas as pd

from stackup.core import calc_worst_case, calc_wc_contributions, calc_rss, calc_rss_contributions

df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()

min_gap_wc, max_gap_wc = calc_worst_case(nominals, plus_tols, minus_tols, directions)
min_gap_rss, max_gap_rss = calc_rss(nominals, plus_tols, minus_tols, directions)

range_wc = max_gap_wc - min_gap_wc
range_rss = max_gap_rss - min_gap_rss
rss_pct_of_wc = range_rss / range_wc * 100

wc_table = calc_wc_contributions(df)
rss_table = calc_rss_contributions(df)

print(f"Worst case: {min_gap_wc:.3f}-{max_gap_wc:.3f} mm (range {range_wc:.3f} mm)")
print(f"RSS: {min_gap_rss:.3f}-{max_gap_rss:.3f} mm (range {range_rss:.3f} mm)")
print(f"RSS range is {rss_pct_of_wc:.0f}% of worst case")

combined = pd.merge(wc_table, rss_table, on="name", suffixes=("_wc", "_rss"))
sorted_result = combined.sort_values("contribution_pct_rss", ascending=False)

sorted_result = sorted_result[["name", "contribution_pct_rss", "contribution_pct_wc"]]

print(sorted_result.round(2).to_string(index=False))
