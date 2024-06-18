inputan = float(input('masukan angka = '))

# enol
enol = (inputan > 0)
print('angka bernilai = ', enol)

minma = (inputan < 5)
print('angka bernilai = ', minma)

uplap = (inputan > 8)
print('angka bernilai = ', uplap)

donelpen = (inputan < 11)
print('angka bernilai = ', donelpen)


print(" ")
encap = enol and minma or uplap and donelpen
print('semua angka bernilai = ', encap)


