import datetime
import os
import string
import random

# templaye dict mhs
mahasiswa_template = {
    'nama':'nama',
    'npm':'00000',
    'sks_lulus':0,
    'lahir':datetime.datetime(2001,9,10)
}

data_mhs = {}

while True:
    os.system("cls")
    print(f"{'WILUJENG SUMPING':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)


    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    print(mahasiswa)
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['npm'] = input("NPM Mahasiswa : ")
    mahasiswa['sks_lulus'] = int(input("SKS lulus Mahasiswa : "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (MM) (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (DD) (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({KEY:mahasiswa})


    # Header tabel
    print(f"{'KEY':<8} {'Nama':<15} {'SKS':<5} {'Lahir':<10}")
    print("-"*50)
    for mahasiswa in data_mhs:
        KEY = mahasiswa

        NAMA = data_mhs[KEY]['nama']
        NPM = data_mhs [KEY]['npm']
        SKS = data_mhs [KEY]['sks_lulus']
        LAHIR = data_mhs [KEY]['lahir'].strftime("%x")

        print(f"{KEY:<8} {NAMA:<15} {SKS:<5} {LAHIR:<10}")

    print("\n")
    is_done = input("sudah? (y/n) \n")
    if is_done == 'Y' or is_done == 'y':
        break
    else:
        continue

print("\n Akhir dari program, terima gaji")



