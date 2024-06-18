kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]


print(f"\nFOR")
for i in kumpulan_angka:
    print(f"data = {i}")

print(f"\nfor loop dan Range")
jumlah_data = len(kumpulan_angka)
for i in range(jumlah_data):
    print(f"data = {kumpulan_angka[i]}")

print(f"\nWhile Loop")
i = 0
while i < jumlah_data:
    print(f"data = {kumpulan_angka[i]}")
    i += 1

print(f"\nList comprehension")
[print(f"data = {i}") for i in kumpulan_angka]
[print(f"angka dipangkatkan 2 = {i**2}") for i in kumpulan_angka]
dgn_prin = [i**2 for i in kumpulan_angka]
print(f"dengan print {dgn_prin}")

print(f"\nEnumerate")
i = 0
for index,data in enumerate(kumpulan_angka):
    print(f"index = {index}, data = {data}")
