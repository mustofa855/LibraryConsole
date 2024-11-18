## Global dan Local scope

nama_global = "otong" # <- variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkna {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel local scope
def fungsi2():
    nama_local = "ucup" # variabel local scope

fungsi2()
# print(nama_local) -> tidak bisa dilakukan

## contoh1: penggunaan akses variabel
nama = "otong"
def say_otong():
    print(f"Hello {nama}")

## contoh 2 : merubah variabel global
angka = 0
def ubah(nilai_baru, nama_baru):
   global angka #fungsi ini mendapat akses merubah angka
   global name
   angka=nilai_baru
   name = nama_baru

print(f"sebelum {angka, name}")
ubah(10,"otong")
print(f"sesudah {angka, name}")

## contoh 3
angka = 0

for i in range(1,5):
    angka += 1
    angka_dummy = 10

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)