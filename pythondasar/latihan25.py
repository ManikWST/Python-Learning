def string(nama):
    print(f"selamat pagi {nama}\n")
string("Manik")

def angka(angka1, angka2):
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}\n")
angka(10,5)

def data_diri(nama, NIM, Kelas):
    print(f"Halo Teman Teman, Perkenalkan Nama Saya {nama}. dan saya memiliki nim {NIM}, dari Kelas {Kelas}\n")
data_diri("Manik", "2201010124", "M")



data_makanan = ["nasi Goreng", "Nasi Padang", "Lontong Sayur", "Sayur Kangkung"]
def list(list_makanan):
    makanan = list_makanan.copy()
    makanan[3] = "Bubur Ayam"
    for makan in makanan:
        print(f"{makan} makanan enak")
list(data_makanan)
print(data_makanan)
