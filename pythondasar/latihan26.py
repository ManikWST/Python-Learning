def kuadrat(angka_drat):
    angka = angka_drat**2
    return angka
a = kuadrat(3)
print(a)

print(kuadrat(4))

b = a + kuadrat(5)
print(b)

def def_tambah(angka1, angka2):
    return angka1 + angka2
e = def_tambah(10,5)
print(e)

def kalku(ang1, ang2):
    tambah = ang1 + ang2
    kurang = ang1 - ang2
    kali = ang1 * ang2
    bagi = ang1 / ang2

    return tambah, kurang, kali, int(bagi)

h,j,k,l = kalku(10,5)
print(f"\n{h}\n{j}\n{k}\n{l}")