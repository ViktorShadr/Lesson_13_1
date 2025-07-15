from pathlib import Path

import pandas as pd

wine_reviews = pd.read_csv(Path("../data/winemag-data-130k-v2.csv"))

print(wine_reviews.shape)
print(wine_reviews.head())

excel_data = pd.read_excel(Path("../data/winemag-data-130k-v2.xlsx"))
print(excel_data.shape)
print(excel_data.head())