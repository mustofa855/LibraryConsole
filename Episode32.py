## Teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a


# ini akan merubah kedua list
a[1] = "michael"
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# address dari kedia list
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# menduplikat data dengan meng copy

print("membuat lust c dengan a.copy()")
c = a.copy() #full duplicate/data baru

print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")
print(f"address a = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b} ")
print(f"c = {c} ")

print("Ubah data 0")
c[0] = "dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Ubah data 1")
a[1] = "dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

