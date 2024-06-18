list_a = [1,2,3]
list_b = [4,5,6]

list_biasa = [1,2,3,4,5,6]
urutan1 = [list_a,list_b, list_biasa, 1, 2, 3]
print(f"list 2 dimensi = {urutan1}")

# data peserta
peserta1 = ["Ucup", 20, "Laki-Laki"]
peserta2 = ["Ujang", 15, "Laki-Laki"]
peserta3 = ["Yanti", 18, "Wanita"]
peserta4 = ["Yuna", 19, "Wanita"]


# data panitia
panitia1 = ["Wayan", 18, "Laki-Laki"]
panitia2 = ["Putu", 20, "Wanita"]
panitia3 = ["Kade", 21, "Wanita"]
panitia4 = ["Made", 20, "Laki-Laki"]


peserta_lomba = [peserta1, peserta2, peserta3, peserta4]

print(f"\n{peserta_lomba}\n")

for peserta in peserta_lomba:
    print(f"Nama Peserta \t: {peserta[0]}")
    print(f"Umur Peserta \t: {peserta[1]}")
    print(f"Gender Peserta \t: {peserta[2]}\n")

edit = peserta_lomba.copy()
print(f"mentahan copy = {edit}\n")
peserta1[0] = "Manik"
print(f"hasil edit {edit}\n")
print(f"list ini harus normal/netral {peserta_lomba}")