data = [1,2,3,4,5,6,7,8,8,9,9,0]

hitung_data = data.count(8)
print(f"data 8 ada berapa ? = {hitung_data}")

data_nama = ["Ujang", "Ucup", "Yasmin", "Putra"]
data_index = data_nama.index("Putra")
print(f"Ucup berletak di urutan Berapa ? = {data_index}")

data.sort()
data_nama.sort()
print(f"data yang diurutkan \n{data} \n{data_nama}")

data.reverse()
data_nama.reverse()
print(f"data yang kebalik \n{data} \n{data_nama}")

