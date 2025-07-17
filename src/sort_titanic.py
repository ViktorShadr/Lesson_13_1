import json

import pandas as pd


sort_passengers_by_avg_grade = pd.read_csv('..//data/titanic.csv')
# result = sort_passengers_by_avg_grade.to_json(orient='records', indent=4)


new_sort = sort_passengers_by_avg_grade.groupby('Sex')['Age'].mean()

new_sort.to_json('..//data/sort_passengers.json', indent=4)

def avg_age_by_gender(df):
    avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
    avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
    result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
    return json.dumps(result_dict)

def avg_age_by_gender_simple(df):
    return df.groupby('Sex')['Age'].mean().round(2).to_json()


print(json.loads(avg_age_by_gender(sort_passengers_by_avg_grade)))
print(json.loads(avg_age_by_gender_simple(sort_passengers_by_avg_grade)))