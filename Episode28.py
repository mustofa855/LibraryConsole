# latihan perulangan membuat segitiga

sisi = 10

# menggunakan for
# dummy variabel
print("Awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count +=1

print("akhir dari for")

# menggunakan while
print("awal dari while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count >= sisi:
        break
    
print("akhir dari while")

# 3 hanya ganjil saja
print("awal dari while")
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    # akan kembali ke atas jika ganjil
    if count % 2 == 0:
        spasi -= 1
        count += 1
        continue
    
    # akan diprint
    print(" "*spasi,"*"*count)
    count += 1


    if count >= sisi:
        break
    
print("akhir dari while")