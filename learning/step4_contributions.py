import pandas as pd
from stackup.core import calc_wc_contributions

df = pd.read_csv("data/housing_stack.csv")
contributions = calc_wc_contributions(df)

print(contributions.round(2).to_string(index=False))

