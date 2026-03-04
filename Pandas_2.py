import pandas as pd
data = pd.read_csv("Titanic-Dataset.csv")
print(data.head())
print(data.info())
no_age = data.dropna(subset= ["Age"])
print(no_age.head(10))
average_age = data["Age"].mean()
data["Age"]= data["Age"].fillna(average_age)
print(data.head(10))