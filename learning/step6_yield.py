import pandas as pd
from stackup import simulate_gaps, calc_pct_out_of_spec, calc_rss, calc_worst_case

lower_limit = 0.35
upper_limit = 0.75

print(f"Requirement: {lower_limit:.3f} to {upper_limit:.3f} mm")

df = pd.read_csv("data/housing_stack.csv")

nominals = df["nominal"].to_numpy()
plus_tols = df["plus_tol"].to_numpy()
minus_tols = df["minus_tol"].to_numpy()
directions = df["direction"].to_numpy()


gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions)
pct = calc_pct_out_of_spec(gaps, lower_limit, upper_limit)

uniform_gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions, distribution="uniform")
uniform_pct = calc_pct_out_of_spec(uniform_gaps, lower_limit, upper_limit)

print(f"Normal: standard deviation {gaps.std():.4f} mm, {pct:.3f}% out of spec")
print(f"Uniform: standard deviation {uniform_gaps.std():.4f} mm, {uniform_pct:.3f}% out of spec")

min_gap_wc, max_gap_wc = calc_worst_case(nominals, plus_tols, minus_tols, directions)
min_gap_rss, max_gap_rss = calc_rss(nominals, plus_tols, minus_tols, directions)

if min_gap_wc >= lower_limit and max_gap_wc <= upper_limit:
    print(f"Worst Case: {min_gap_wc:.3f} to {max_gap_wc:.3f} mm, PASS")
else:
    print(f"Worst Case: {min_gap_wc:.3f} to {max_gap_wc:.3f} mm, FAIL")

if min_gap_rss >= lower_limit and max_gap_rss <= upper_limit:
    print(f"RSS: {min_gap_rss:.3f} to {max_gap_rss:.3f} mm, PASS")
else:
    print(f"RSS: {min_gap_rss:.3f} to {max_gap_rss:.3f} mm, FAIL")
