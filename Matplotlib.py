import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x, y, "b-")
plt.axis([0, 10, 0, 200])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample Graph")
plt.legend()
plt.show()