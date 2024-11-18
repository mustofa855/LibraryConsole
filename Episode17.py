# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case

salam = "bro salam"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lowe case
alay = "AkU KeCe ABIEzzZZZ"
print("normal = "+alay)
alay = alay.lower()
print("lower = "+alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + "is lower = "+ str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + "is upper = "+ str(apakah_upper))

# isalpha() --> mengecek apakah semuanya huruf
# isalnum() --> huruf dan angka
# isdecimal() --> angka saja
# isspace() --> spasi, tab, newline
# istitle() --> semua kata diawali huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() 
print(judul+" is title? "+ str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " +str(cek_start))

cek_end = "Sangjangnim Oppa".startswith("Oppak")
print("end = " +str(cek_end))

## Penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = 'akuehmsayangehmkamu'
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = "tengah".strip(":")
print("'"+tengah+"'")
