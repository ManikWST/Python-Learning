import os
os.system("cls")
def keyward(**keywod):
    nama = keywod["nama"]
    nim = keywod["nim"]
    kelas = keywod["kelas"]
    print(f"namnya adalah {nama} dan dia memiliki NIM {nim}, yang berada di kelas {kelas}")
keyward(nama="Manik", nim=2201010124, kelas="M")

def gabung(*args,**keywods):
    if keywods["option"] == "tambah":
        output = 0
        for angka1 in args:
            output += angka1
    elif keywods["option"] == "kali":
        output = 1
        for angka2 in args:
            output *= angka2
    return output
tambah = gabung(1,2,3,4, option="tambah")
print(tambah)
kali = gabung(1,2,3,4, option="kali")
print(kali)