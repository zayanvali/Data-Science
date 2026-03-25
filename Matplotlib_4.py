import matplotlib.pyplot as plt
import pandas as pd
ages = [1, 7, 10, 17, 11, 15, 19, 21, 27, 33, 39, 37, 40, 43, 45, 47, 48, 57, 72, 79]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins, histtype = "stepfilled", rwidth = 0.8)
plt.title("Histogram")
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.show()