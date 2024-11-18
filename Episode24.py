# perulangan (loop)

# for kondisi:
#     aksi

# pengulangan menggunakan list
angka2_1 = [0,1,2,3,4,5] # ini adalah list
print(angka2_1)

for i in angka2_1:
    print(f"i sekarang -> {i}")

print("akhir dari program\n")

# pengulangan menggunakan range
angka2_range = range(5)

for i in range(5):
    print(f"i sekarang -> {i}")

print("akhir dari program 2\n")

# pengulangan menggunakan range
angka2_range = range(1,5)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 3\n")

# menggunakan string
data_str = "saya ganteng abis"
for huruf in data_str:
    print(huruf)
print("akhir dari program 4\n")
