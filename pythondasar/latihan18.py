a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

data = [a, b, 5, 10]

print(f"data gabung ASLI {data}")

data_copy = data.copy()
print(f"data copy {data_copy}\n")
data_copy[0][0] = 40
print("perbandingan data yang di edit")
print(f"data asli = {data}")
print(f"data copy = {data_copy}\n")

from copy import deepcopy
data = [a, b, 5, 10]

data_baru_cp = deepcopy(data)
data_baru_cp[0][0] = 50
print(f"data deep copy {data_baru_cp}")
print(f"data asli {data}\n")
