# Width and Multiline

# Data

data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+" data string "+5*"=")
print(data_string)

# string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(5*"="+" data string "+5*"=")
print(data_string)

# string multiline (kutip triplets)

data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(5*"="+" data string "+5*"=")
print(data_string)

# mengatur lebarnya
data_nama = "ucup"
data_string = f"""nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print(5*"="+" data string "+5*"=")
print(data_string)





