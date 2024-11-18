# Input User

# data yang dimasukkan pasti string
data = input("Masukan Data : ")

print("data = ",data,", type = ", type(data))

# jika kita ingin mengambil int, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))

print("data = ",angka,", type = ", type(angka))

# bagaimana dengan boolean
data_bool = bool(int(input("masukkan nilai boolean : ")))

print("data = ",data_bool,", type = ", type(data_bool))
