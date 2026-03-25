import matplotlib.pyplot as plt
import pandas as pd
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 1, 0.5, 1, 0.4, 1, 0.7, 1, 0.67]
plt.scatter(x, y, label = "Scatter", color = "Red", marker = "o", s = 50)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()