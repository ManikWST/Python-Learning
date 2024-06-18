import os
os.system("cls")
def coba1(nama, tinggi, berat):
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")
coba1("ucup", 120, 50)

def coba2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"namanya {nama} dia memiliki tinggi {tinggi} dan beratnya {berat}")
coba2(["Dudung", 110, 55])

def coba3(*args):
    nama = args[0]
    nim = args[1]
    kelas = args[2]
    domisili = args[3]
    print(f"namanya {nama} dia memiliki NIM {nim} dan berada di kelas {kelas}, yang berdomisili di kabupaten {domisili}")
coba3("Manik", 2201010124, "M", "Tabanan")

def coba4(*argsfor):
    awal = 0
    for angka in argsfor:
        awal += angka
    return awal
datafor = coba4(4,10,10)
print(f"totalnya = {datafor}")
