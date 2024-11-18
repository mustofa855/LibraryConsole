# Date and time (latihan)

import datetime as dt
import locale

# Mengatur locale ke bahasa Indonesia
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

# hari_ini = dt.date.today()

# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2002,2,22)
# print(tanggal)
# print(f"Hari lahir adalah hari = {tanggal:%A}")

print("Silakan masukkan tanggal,\nbulam dan tahun lahir anda \n")

tanggal = int(input("Tanggal\t:"))
bulan = int(input("Bulan\t:"))
tahun = int(input("Tahun\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal_lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"Bulannya adalah : {tanggal_lahir:%B}")
print(f"umur anda adalah {umur_tahun} tahun, {umur_bulan_sisa} bulan")

