def pangkatan(nulai):
    return nulai**2
a = pangkatan(3)
print(a)

kuadrat = lambda hitung : hitung**2
print(f"kuadrat 5 = {kuadrat(5)}")
kdrat = lambda htung,pngkat : htung**pngkat
print(f"hasil kuadrat = {kdrat(3,2)}")

data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"data hasil sort {data_list}")

def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"data hasil sort {data_list}")

data_list = ["Otong", "Ucup", "Dudung"]

data_list.sort(key=lambda nama : len(nama))
print(f"data hasil sort {data_list}")



data_angka = [1,2,3,4,5,6,7,8,9,10]

# def ambil_angka(angka):
#     return angka < 5

ambil_angka = lambda angka : angka<5
tampil_data = list(filter(ambil_angka, data_angka))
print(f"Tampil Data = {tampil_data}")

angka_genap = lambda genap : genap%2==0
tampil_genap = list(filter(angka_genap, data_angka))
print(f"List Genap = {tampil_genap}")

angka_ganjil = lambda ganjil : ganjil%2!=0
tampil_ganjil = list(filter(angka_ganjil, data_angka))
print(f"List Ganjil = {tampil_ganjil}")

angka_3 = lambda tigas : tigas%3==0
tampil_3 = list(filter(angka_3, data_angka))
print(f"angka kelipatan 3 = {tampil_3}")