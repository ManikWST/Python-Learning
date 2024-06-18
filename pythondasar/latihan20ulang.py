list_buku = []

while True:
    print("\nMasukan Data Buku Baru")
    nama_buku = input("Masukan Judul Buku \t: ")
    penulis_buku = input("Masukan Penulis Buku \t: ")
    penerbit = input("Masukan Nama Penerbit \t: ")
    tahun_terbit = input("Masukan Tahun Terbit \t: ")

    buku_baru = [nama_buku, penulis_buku, penerbit, tahun_terbit]
    list_buku.append(buku_baru)
    
    print("\nNo. \t|\t Judul Buku \t|\t Penulis Buku \t|\t Penerbit Buku \t|\t Tahun Terbit")
    for index,data in enumerate(list_buku):
        print(f"{index+1} \t|\t {data[0]} \t|\t {data[1]} \t|\t {data[2]} \t|\t {data[3]}")

    tanyakan = input("apakah anda ingin melanjutkan menambah data baru ? (Y/N) ")

    if tanyakan == "n" or tanyakan == "N":
        break
print("DATA BERHASIL DI BUAT")