kum_data = ["kuman", "jamal", "susanti", "yanti", "beruang"]
print(f"\ndata Normal {kum_data}\n")

inputan_data = input("masukan data yang ingin di tambah : ")
inputan2_data = input("masukan data berikutnya untuk insert : ")


kum_data.append(inputan_data)
print(f"\n 4. data yang ditambah {kum_data}\n")

kum_data.insert(0,inputan2_data)
print(f" 5. data yang di insertkan adalah {kum_data}\n")

cek_data = len(kum_data)
print(f" 3. berapa total data yang ada ? = {cek_data}\n")

ambil_ke1 = kum_data[0]
print(f" 1. data pertama adalah =  {ambil_ke1}\n")

ambil_kelast = kum_data[-1]
print(f" 2. ambil data terakhir adalah = {ambil_kelast}\n")

data_baru = ["kelinci", "macan", "singa"]
data_baru.extend(kum_data)
print(f"data gabungan adalah = {data_baru}")


kum_data[0] = "MANIK"
print(f"hasil edit data baru {kum_data}")

kum_data.remove(kum_data[-1])
print(f"data yang telah dihapus disini adalah = {kum_data}")

