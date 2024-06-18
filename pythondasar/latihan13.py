data_int = [0, 1, 2, 3, 4]
print(data_int)

data_str = ["i", "komang", "manik", "wastika"]
print(data_str)

data_bool = [True, True, False, True]
print(data_bool)

# data_camp = [1, "i", True, 2, "komang", True, 3, "manik", False, 4, "wastika", True]
# print(data_camp)

tstdata_camp = [data_int[0], data_str[0], data_bool[0], data_int[1], data_str[1], data_bool[1], data_int[2], data_str[2], data_bool[2], data_int[3], data_str[3], data_bool[3]]
print(tstdata_camp)

range_list = range(0,10)
list_range = list(range_list)
print(f"ini adalah list biasa {list_range}")

listpang = [i**2 for i in range(0,10)]
print(f"ini di pangkatkan 2 hasilnya adalah {listpang}")

listgenap = [i for i in range(0,10) if i %2 == 0]
print(f"hasil print genap dengan modulus {listgenap}")

listganjil = [i for i in range(0,10) if i %2 != 0]
print(f"hasil print ganjil dengan medulus {listganjil}")

