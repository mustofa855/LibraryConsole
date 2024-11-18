# data_input = int(input("masukkan angka : "))

# hasil = 10/data_input

# print(hasil)

# file = open("Episode66/data.txt",'r') # padahal file data.txt ngga ada

# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
# input_user = int(input("Masukkan angka : "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh nol(0)")

# print(f"hasil = {hasil}")

## contoh di aplikasi

while(True):
    angka = int(input("masukkan angka pembagi : "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan?? (y/n)")
        if is_done == 'n' or is_done == "N":
            break
    except:
        print("pembagi nol, silakan masukkan input lagi")

print("akhir dari program")
# contoh aplikasi untuk membuat file data.txt
try:
    with open("Episode66/data.txt",'r') as file:
        print("Isi file = \n",file.read())
except:
    print("data.txt tidak ditemukan, membuat file baru")
    with open("Episode66/data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")
print("akhir program 2")