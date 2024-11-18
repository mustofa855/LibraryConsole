"""
    Buat program yang menerima dua input angka dari 
    pengguna dan menghitung hasil dari operasi penjumlahan,
    pengurangan, perkalian, pembagian, dan sisa bagi.
"""

print("OPERASI ARITMATIKA")
angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))

print("PENJUMLAHAN")
hasil = angka1 + angka2
print(f"{angka1} + {angka2} = ", hasil)


print("PENGURANGAN")
hasil = angka1 - angka2
print(f"{angka1} - {angka2} = ", hasil)


print("PERKALIAN")
hasil = angka1 * angka2
print(f"{angka1} x {angka2} = ", hasil)


print("PEMBAGIAN")
hasil = angka1 / angka2
print(f"{angka1} / {angka2} = ", hasil)


print("HASIL BAGI")
hasil = angka1 % angka2
print(f"{angka1} % {angka2} = ", hasil)
