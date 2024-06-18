# manipulation str
nama_awal = "I komang"
nama_tengah = "Manik"
nama_akhir = "Wastika"
nama_lengkap = " " + nama_awal + " " + nama_tengah + " " + nama_akhir
print("nama lengkap adalah :" + nama_lengkap)

# jumlah str lalu di manipulasi
jumlah = len(nama_lengkap)
print("jumlah hurup dari namaku : " + str(jumlah))

# temukan str lalu manipulasi
find = "M"
them = find in nama_lengkap
print("apakah m ada dalam nama lengkap ? " + str(them))

find = "j"
them = find in nama_lengkap
print("apakah m ada dalam nama lengkap ? " + str(them))

find = "j"
them = find not in nama_lengkap
print("apakah m ada dalam nama lengkap ? " + str(them))

# perulangan str
print("kiw"*10)

# indexing
print("index ke 0 dari nama lengkap adalah = " + nama_lengkap[3])
print("index ke 16 dari nama lengkap adalah = " + nama_lengkap[16])
print("index ke -10 dari nama lengkap adalah = " + nama_lengkap[-10])
print("index ke 1 sampai 8 dari nama lengkap adalah = " + nama_lengkap[3:9])
print("index ke 3 sampai 23 dari nama lengkap adalah = " + nama_lengkap[3:24:2])
gabungan = nama_lengkap[3] + nama_lengkap[-10] + nama_lengkap[16] + " "
print("helo cewek, " + gabungan*2)

# menghitug jumlah hurup penggunakan copunt

namaini = "manik wastika"
hitung = namaini.count("a")
print("total hurup i pada namaini adalah = " + str(hitung))

namaini = namaini.upper()
print("jadi uppercase " + namaini)



