data = {
    "cup" : "Ucup Surucup",
    "ags" : "Agus Sudarjo",
    "mkl" : "Muklis Arimawan"
}

ukuran = len(data)
print(f"panjang data adalah {ukuran}")

key = "cup"
cek = key in data
print(f"apakah cup ada di data = {cek}")


#get data
data1 = data["cup"]
print(f"data pertama {data1}")
data2 = data.get("mkl")
print(f"{data2}")

#update atau edit
#update
data["cup"] = "Otong Surotong"
data3 = data.get("cup")
print(f"edit ucup = {data3}")
#tambah
data["sep"] = "Asep Sukasep"
print(f"data tambah sep = {data}")


del data["sep"]
print(f"data removers = {data}")