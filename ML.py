import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df["Age"].fillna(df["Age"].mean(), inplace = True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace = True)
df.drop("Cabin", axis = 1, inplace = True)
df["Sex"] = df["Sex"].map({"male":0, "female": 1})
df = pd.get_dummies(df, columns = ["Embarked"])
print(df.head(20))