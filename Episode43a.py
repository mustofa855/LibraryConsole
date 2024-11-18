import datetime
import os

# templaye dict mhs
mahasiswa_template = {
    'nama':'nama',
    'npm':'00000',
    'sks_lulus':0,
    'lahir':datetime.datetime(2001,9,10)
}

data_mhs = {}

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

print(mahasiswa)



