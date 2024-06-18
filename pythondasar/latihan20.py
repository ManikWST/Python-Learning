list_buku = []
while True:
    print("\n Welcome to Perpustakaan Manik")
    nama_buku = input("Masukan Judul Buku \t: ")
    penulis = input("Masukan Nama Penulis \t: ")
    penerbit = input("Masukan Nama Penerbit \t: ")
    tahun_terbit = input("Masukan Tahun Terbit \t: ")

    buku_baru = [nama_buku, penulis, penerbit, tahun_terbit]
    list_buku.append(buku_baru)


    print("\nNo.\t|\t Nama Buku \t|\t Nama Penulis \t|\t Penerbit \t|\t Tahun Terbit")
    for index,data in enumerate(list_buku):
        print(f"{index+1}\t|\t{data[0]}\t|\t{data[1]}\t|\t{data[2]}\t|\t{data[3]}")

    qouestion = input("apakah ingin lanjut input data ? (Y/N) ")

    if qouestion == "n" or qouestion == "N":
        break
print("Program Selesai")