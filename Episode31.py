# operasi list
data_angka = [9,4,2,7,0,1,3,5,7,3,6,9,8]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah data angka 4 ={jumlah_data_4}")
print(f"jumlah data angka 4 ={jumlah_data_3}")

# ambil posisi data (index)
data = ["ucup", "otong", "dudung", "ujang"]
print(f"data = {data}")

index_dudung = data.index("dudung")
index_ujang = data.index("ujang")

print(f"index si dudung = {index_dudung}")
print(f"index si ujang = {index_ujang}")

# mengurutkan list
print(f"data angka sebelum di sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = \n{data}")

# balik listnya
data_angka.reverse()
data.reverse()

print(f"data direverse = \n {data_angka} \n {data}")


