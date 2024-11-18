# Latihan percabangan

# Kalkulator sederhana
print(20*"=")
print("kalkulator sederhana".upper())
print(20*"="+"\n")

angka1 = float(input("masukkan angka pertama = "))
operator = input("masukkan operasi (+,-,x,/) = ")
angka2 = float(input("masukkan angka kedua = "))

# percabangannya
if operator == "+":
    hasil = angka1+angka2
    print(f"hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
    print(f"hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka1 /angka2
    print(f"hasilnya adalah = {hasil}")
else:
    print("operator tidak diketahui")

print("terima gaji")