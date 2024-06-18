a = ["manik", "ucup", "Dadang", "Yunas"]

print(f"berikut adalah data a = {a}")

b = a
print(f"data b adalah sebagai berikut {b}")

c = a.copy()

b[0] = "Wastika"
a.sort()
c[0] = "Jamal"
print(f"data belum copy \nA{a} \nB{b} \nC{c}")
