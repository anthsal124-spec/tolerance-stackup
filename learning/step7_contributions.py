import pandas as pd
import matplotlib.pyplot as plt

from stackup import calc_wc_contributions, calc_rss_contributions
from plots import plot_contributions

df = pd.read_csv("data/housing_stack.csv")

wc_table = calc_wc_contributions(df)
rss_table = calc_rss_contributions(df)

combined = pd.merge(wc_table, rss_table, on="name", suffixes=("_wc", "_rss"))
sorted_result = combined.sort_values("contribution_pct_rss", ascending=False)

sorted_result = sorted_result[["name", "contribution_pct_rss", "contribution_pct_wc"]]

title = "Contribution of each dimension to gap variation, housing stack"

fig, ax = plot_contributions(sorted_result, title)

fig.savefig("plots/contributions.png", dpi=150, bbox_inches="tight")
plt.show()
