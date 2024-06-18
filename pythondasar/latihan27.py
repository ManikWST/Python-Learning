def salam(nama, salam = "apa kabar!!"):
    print(f"Halo {nama}, {salam}")
salam("manik","kamu sehat ?")
salam("wastika")

def pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil
a = pangkat(pangkat=2, angka=5)
print(a)

def buanyak(angka1=1, angka2=2, angka3=3, angka4=4):
    jumlah = angka1 + angka2 + angka3 + angka4
    return jumlah
a = buanyak(angka4=10)
print(a)
