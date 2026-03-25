import matplotlib.pyplot as plt
import pandas as pd
slices = [6, 1, 12, 1, 3]
activities = ["Sleep", "Eat", "Work", "Hangout", "Friends"]
colour = ["c", "m", "r", "b", "g"]
plt.pie(slices, labels = activities, colors = colour, startangle = 90, shadow = True)
plt.show()