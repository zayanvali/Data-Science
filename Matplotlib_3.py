import matplotlib.pyplot as plt
import pandas as pd
data  = pd.read_csv("Titanic-Dataset.csv")
actual_top = data.sort_values(by = "Fare", ascending = False).head(30)
actual_top = actual_top.reset_index(drop = True)
plt.plot(actual_top.index, actual_top["Fare"], marker = "o", linestyle = "-", color = "b")
plt.title("Highest Titanic Fare")
plt.xlabel("PassengerIndex 0-29")
plt.ylabel("Fare Value")
plt.grid(True, linestyle =  "--")
plt.show()
