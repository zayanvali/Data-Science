import numpy as np
new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(new_arr[:7])
print(new_arr[::2])
print(new_arr[::-1])
multi_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multi_arr[0:1, 0:1])
print(multi_arr[1:2, 1:2])
k = np.array([1, 2, 3, 4, 5, 6, 7, 8])
even_arr = k[k % 2 == 0]
print(even_arr)
bool = k[k == 5]
print(bool)
sample_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0,len(sample_list)):
    sample_list[i] += 1
print(sample_list)
k += 1
print(k)