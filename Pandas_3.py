import pandas as pd
data = pd.read_csv("Titanic-Dataset.csv")
print(data.head(10))
average_age = data["Age"].mean()
data["Age"]= data["Age"].fillna(average_age)
twenty_forty = data[(data["Age"]>20)&(data["Age"]<40)]
print(twenty_forty[["Name", "Fare"]].head())
fare_100 = data[(data["Fare"]>100)]
print(fare_100[["PassengerId", "Name", "Pclass"]].head())
data.iloc[0:5, data.columns.get_loc("Name")]= "Test"
print(data[["Age", "Name"]].head())
data.iloc[11:16, data.columns.get_loc("Fare")]= 999
print(data.loc[11:15, ["Name", "Fare"]])
data["FarePerPerson"]= data["Fare"]/(data["SibSp"]+ 1)
print(data[["Name", "FarePerPerson"]].head())
data["IsAlone"]= (data["SibSp"]== 0) & (data["Parch"])
print(data.head())
