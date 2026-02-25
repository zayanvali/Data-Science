import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_3 = arr-2
print(arr_3)
arr_2 = arr*3
print(arr_2)
for i in range(0,len(arr)):
    arr[i] += 5
print(arr)
