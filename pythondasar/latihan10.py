# nama = input("Masukan Nama Pemilik : ")

# if nama=="manik":
#     print(f"halo {nama} welcome to your program")
#     print("real manik")
# else:
#     print(f"WOI SIPAA KAMU {nama} anjing PENYUSUP!!!")
#     print("kamu BUkan Manik")


angka_awal = float(input("masukan angka awal : "))
operator = input("masukan operator (+, -, x, /) : ")
angka_akhir = float(input("Masukan angka akhir : "))

if operator=="+":
    hasil = angka_awal + angka_akhir
    print(f"hasil dari {angka_awal} + {angka_akhir} = {hasil}")
elif operator=="-":
    hasil = angka_awal - angka_akhir
    print(f"hasil dari {angka_awal} - {angka_akhir} = {hasil}")
elif operator=="*" or operator=="x":
    hasil = angka_awal * angka_akhir
    print(f"hasil dari {angka_awal} x {angka_akhir} = {hasil}")
elif operator=="/":
    hasil = angka_awal / angka_akhir
    print(f"hasil dari {angka_awal} / {angka_akhir} = {hasil}")
else:
    print("tolong masukan operator sesuai ketentuan")