# '''Latihan fungsi'''

import os

# # program untuk menghitung luas dan keliling persegi panjang

# # membuat header program
# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{40*'-':^40}")

# # mengambil input user
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")

def header():
    # membuat header program
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{40*'-':^40}")

def input_user():
    '''Fungsi input user'''
    # mengambil input user
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))

    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''Fungsi luas'''
    # program menghitung luas 
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''Fungsi keliling'''
    return 2*(lebar+panjang)
  
def display(message, value):
    '''Fungsi display'''
    print(f"hasil perhitungan {message} = {value} ")

# program utamanya
while True:
    header()

    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    display("luas : ", LUAS)
    display("keliling : ", KELILING)

    isContinue = input("Apakah lanjut (y/n) : ")
    if isContinue == "n":
        break

print("program selesai, terima gaji")