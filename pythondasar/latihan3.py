
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
z = 5

# five = a | z 
# print('penjumlahan serta OR========')
# print('nilai a adalah ', a, 'dan binerynya adalah ', format(a, '08b'))
# print('nilai z adalah ', z, 'dan binerynya adalah  ', format(z, '08b'))
# print('========OR===========')
# print('hasil dar adalah', five, 'dan binerynya adalah', format(five, '08b'))


# format binery
# VARIABLE HARUS BERTIPE INT!!!!!!
z = 5
x = 10

print("======OR=======")
one = z | x
print('nilai z adalah ', z, "dan binerynya adalah ", format(z, '08b'))
print('nilai x adalah ', x, 'dan binerynya adalah', format(x, '08b'))
print('=========================')
print('hasil dari or ', one, 'dan binernya adalah  ', format(one, '08b'))


print("=====AND======")
two = z & x
print('nilai z adalah ', z, 'dan binerynya adalah ', format(z, '08b'))
print('nilai x adalah ', x, 'dan binerynya adalah', format(x, '08b'))
print('==========================')
print('hasil dari and ', two, ' dan binernya adalah ', format(two, '08b'))

print('=====XOR=====')
three = z ^ x
print('nilai z adalah ', z, 'dan binerynya adalah ', format(z, '08b'))
print('nilai x adalah ', x, 'dan binerynya adalah', format(x, '08b'))
print('==========================')
print('hasil dari XOR ', three, 'dan binernya adalah ', format(three, '08b'))

print('====modulus==== -11')
four = ~x
print('nilai x adalah ', x, 'dan binerynya adalah ', format(x, '08b'))
print('nilai fr adalah', four, 'dan binerynya adalah', format(four, '08b'))