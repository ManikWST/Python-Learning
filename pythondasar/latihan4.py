# penjumlahan menggunakan =
a =  10
print('nilai a = ', a)

a += 1
print('nilai a = ', a)

a -= 1
print('nilai a = ', a)

a *= 2
print("nilai a = ", a)

a /= 2
print('nilai a = ', a)

# MODULUS, PANGKAT, BULTKAN, OR, AND, XOR, GESER, teraning ~

b = int(a)
# b %= 2
# print('nilai a adalah ', b)

# b //= 3
# print('nilai a adalah ', b) hasil = 3

# b **= 2
# print('nilai a adalah ', b) hasil = 100

# ====== OR ========
print('==========OR===========')
x = True
print('nilai x adalh ', x)
x |= False
print('nilai x adalah ', x)
x = False
print('nilai x adalah ', x)
x |= False
print('nilai x adalah ', x)

# ====== AND ========
print('==========AND===========')
z = True
print('nilai z adalah ', z)
z &= True
print('nilai z adalah ', z)
z = True
print('nilai z adalah ', z)
z &= False
print('nilai z adalah ', z)

# ====== XOR ========
print('==========XOR===========')
c = True
print('nilai c adalah ', c)
c ^= True
print('nilai c adalah ', c)
c = True
print('nialai c adalah ', c)
c ^= False
print('nilai c adalah ', c)

# ====== Geser ========
print('==========Geser===========')
m = 0b01000
print('bienry dari m adalah', format(m, '05b'))
m >>= 2
print('binery dari m adalah', format(m, '05b'))
m <<= 1
print('binery dari m adalah ', format(m, '05b'))

# ====== ~ ========
print('========== ~ ===========')
g = ~b
print('nilai g adalah ', g)
v = ~g
print('nilai v kebalikan +1 dari 10 adalah ', v)


# OR, AND, XOR
print('=========OR, AND, XOR=========')
print('TRUE')
a = True
print('nilai a adalah = ', a)
a |= False
print('nilai a dari or adalah ', a)
a &= True
print('nilai a dari and adalah ', a)
a ^= False
print('nilai a dari xor adalah ', a)

# OR, AND, XOR
print('=========OR, AND, XOR=========')
print('False')
a = False
print('nilai a adalah = ', a)
a |= False
print('nilai a dari or adalah ', a)
a &= False
print('nilai a dari and adalah ', a)
a ^= False
print('nilai a dari xor adalah ', a)



