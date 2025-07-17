import json

import pandas as pd

def sort_by_age(df):
	filtered_passengers = df[(df['Sex'] == 'male') & (df['Age'] > 50) | (df['Sex'] == 'female') & (df['Age'] < 30)]
	return filtered_passengers.to_json(orient='records', indent=4)

titanic = pd.read_csv('../data/titanic.csv')
print(sort_by_age(titanic))