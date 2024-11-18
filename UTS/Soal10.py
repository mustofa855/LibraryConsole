print("PROGRAM MASUKAN BARANG")

jumlah_brg = int(input("Mau masukin berapa? "))
produk_list = []
harga_list = []

for jumlah in range(jumlah_brg):
    produk = input("Masukkan Barang : ")
    harga = float(input("Harga Barang : "))
    produk_list.append(produk)
    harga_list.append(harga)

print(f"|{'Produk':<15}|{'Harga':>10}|")
print("-" * 28)
for i in range(jumlah_brg):
    print(f"|{produk_list[i]:<15}|{harga_list[i]:>10.2f}|")