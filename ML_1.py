import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("iris.csv")
data["species"] = data["species"].replace({"setosa": 0, "versicolor": 1, "virginica": 2})
plt.subplot(221)
plt.scatter(data["petal_length"], data["species"], s = 10, c = "green", marker = "o")
plt.scatter(data["petal_width"], data["species"], s = 10, c = "green", marker = "o")
plt.scatter(data["sepal_length"], data["species"], s = 10, c = "green", marker = "o")
plt.scatter(data["sepal_width"], data["species"], s = 10, c = "green", marker = "o")
plt.show()
y = data["species"]
x = data.drop("species", axis = 1)
print(x.head())
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
print(x_train.shape)
print(x_test.shape)
model = DecisionTreeClassifier(max_depth = 3, random_state = 1)
model.fit(x_train, y_train)
perdictions = model.predict(x_test)
print("Accuracy ", metrics.accuracy_score(predictions, y_test))