import pandas as pd
data  = pd.read_csv("Titanic-Dataset.csv")
print(data.head())
print(data.info())
name_and_age = data[["Name", "Age", "Survived"]]
print(name_and_age.head())
above_25 = data[data["Age"]>25]
print(above_25.head())
above_25_new = name_and_age[name_and_age["Age"]>25]
print(above_25_new.head())
class_2_or_3 = data[(data["Pclass"]== 2)|(data["Pclass"]== 3)]
print(class_2_or_3[["Name", "Age", "Pclass"]].head())
male_1 = data[(data["Sex"]== "male")&(data["Pclass"]== 1)]
print(male_1.head())
twenty_forty = data[(data["Age"]>20)|(data["Age"]<40)]
print(twenty_forty[["Name", "Fare"]].head())
fare_over_100 = data[data["Fare"]>100]
print(fare_over_100[["PassengerId", "Name", "Pclass"]].head())
survived_3 = data((data["Survived"]== 1)|(data["Pclass"]== 3))
print(survived_3[["Name"]].head())
