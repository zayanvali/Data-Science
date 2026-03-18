import matplotlib.pyplot as plt
plt.plot([1, 4, 7, 9, 10], [2, 8, 14, 18, 20], "r--", label = "y = x*2", linewidth = 5)
plt.plot([1, 4, 7, 9, 10], [3, 12, 21, 27, 30], "g--", label = "y = x*3", linewidth = 2)
plt.axis([0, 5, 0, 50])
plt.legend()
plt.show()