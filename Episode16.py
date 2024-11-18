# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_depan = "ucup"
nama_tengah = "D"
nama_belakang = "martinez"

nama_lengkap = nama_depan+" "+nama_tengah+" "+nama_belakang
print(nama_lengkap)

# 2. Meghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari "+ nama_lengkap + "=" + str(panjang))

# operator untuk string

# mengecek apakah ada komponen char atau  string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di" + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di" + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di" + nama_lengkap + " = " + str(status))

# mengulang string
print(15*"wk")
print("wk"*11)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:10] : " + nama_lengkap[3:10])
print("index ke-[0,2,4,6,8,10,12] : " + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code spasi adalah " + str(ascii_code))
data = 210
print("char untuk ASCII 210 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o") #data -> adalah objek count -> adalah methodnya 
print("jumlah o pada "+data+" = "+ str(jumlah))


