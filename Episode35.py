# looping dari list

# for loop
print(5*"....","for loop","...."*5)
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", "otong","diding","dudung"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print(5*"....","for loop dan range","...."*5)
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)


for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print(5*"....","while","...."*5)
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehention
print(5*"....","list comprehention","...."*5)
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data] # ini cara list comprehension

angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print(5*"....","enumerate","...."*5)
data_list = ["ucup",1,2,3,"otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
