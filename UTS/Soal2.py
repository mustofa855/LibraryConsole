"""
    Tulis kode yang meminta pengguna memasukkan angka 
    dan konversikan input tersebut menjadi integer, 
    lalu tampilkan hasilnya.
"""

nama = input("Masukkan nama anda :")
umur = input("Masukkan umur anda :")
berat_badan = float(input("masukkan berat badan anda dalam kg :"))

umur = int(umur)

print("Nama : ", nama, type(nama))
print("Umur : ", umur, type(umur))
print("BB : ", berat_badan, type(berat_badan))