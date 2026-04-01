import matplotlib.pyplot as plt
import pandas as pd
data  = pd.read_csv("Titanic-Dataset.csv")
x = data.sort_values(by = "Age", ascending = True).head(30)
y = data[["SibSp"]]
plt.plot(x, y, "b-")
plt.axis([0, 30, 0, 4])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()