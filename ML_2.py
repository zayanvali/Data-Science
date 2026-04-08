import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
df = pd.get_dummies(df, columns = ["Survived"])
print(df.head(20))