import matplotlib.pyplot as plt
import pandas as pd
data  = pd.read_csv("Titanic-Dataset.csv")
acsending_fare = data.sort_values(by = "Fare", ascending = True).head(30)
acsending_fare = acsending_fare.reset_index(drop = True)
actual_top = data.sort_values(by = "Fare", ascending = False)
actual_top = acsending_fare.reset_index(drop = True)
plt.plot(actual_top, actual_top["Fare"], marker = "o", linestyle = "-", color = "b")
plt.title("Highest Titanic Fare")
plt.xlabel("PassengerIndex 0-29")
plt.ylabel("Fare Value")
plt.grid(True, linestyle =  "--")
plt.show()