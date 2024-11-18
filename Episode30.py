# Operasi

# index  0(-3)   1(-2)    2(-1)
data = ["ucup", "otong","dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_last = data[-1]
print(f"data terakhir adalah = {data_last}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah
panjang_data = len(data)
print(f"panjangan data = {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("jajang")

# menggabungkan list dengan list
data_baru = ["ujang", "usep", "dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data kedua menjadi michael
data[2] = "michael"
print(f"data update = {data}")

# meremove data
data.remove("ujang")
print(f"data remove = {data}")
# data.remove("Ujang") -> akanh error karena huruf harus sesuai dengan "ujang"

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = {data}")

print(data_akhir)



