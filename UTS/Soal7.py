# Soal 9: Buat program yang mendemonstrasikan penggunaan 
# operator assignment (+=, -=, *=, /=, %=, **=).

angka = float(input("Masukkan angka : "))
print("assign 1 (+=)")
print("assign 2 (-=)")
print("assign 3 (*=)")
print("assign 4 (/=)")
print("assign 5 (%=)")
print("assign 6 (**=)")
pilih = int(input("angkanya mau digimanain pilih assign ! 1-6\n"))


if pilih == 1:
    angka += 5
    print("assignment += 5 ")
    print(angka)
elif pilih == 2:
    angka -= 5
    print("assignment -= 5 ")
    print(angka)
elif pilih == 3:
    angka *= 5
    print("assignment *= 5 ")
    print(angka)
elif pilih == 4:
    angka /= 5
    print("assignment /= 5 ")
    print(angka)
elif pilih == 5:
    angka %= 5
    print("assignment %= 5 ")
    print(angka)
elif pilih == 6:
    angka **= 5
    print("assignment **= 5 ")
    print(angka)
else:
    print("masukin apa sihhh")

print("MAKASIIII")