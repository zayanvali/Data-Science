import matplotlib.pyplot as plt
import numpy as np

#histogram
ages = [10, 17, 21, 29, 31, 36, 45, 56, 63]
bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins, edgecolor = "black", color = "red")
plt.title("Frequency of Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#pie chart
sections = [25, 15, 37, 11, 12]
activities = ["Sports", "Videogames", "TV", "Studying", "Eating"]
colors = ["blue", "red", "green", "yellow", "purple"]
plt.pie(sections, labels = activities, colors = colors, startangle = 90, autopct = '%1.1f%%')
plt.title("Pie Chart of Activities")
plt.axis("equal")
plt.show()