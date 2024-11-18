# 1. mode write

# 'w'
# dia akan membuat file baru jika tidak ada
# lalu akan menimpa overwrite isinya
# menghapus isinya kemudian diganti dengan yang baru 

with open("Episode65/data_1.txt", 'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("Episode65/data_1.txt", 'w',encoding="utf-8") as file:
    file.write("ojon siojon")

with open("Episode65/data_1.txt", 'w',encoding="utf-8") as file:
    file.write("overwrite")

# 2. mode append
with open("Episode65/data_2.txt", 'w',encoding="utf-8") as file:
    file.write("ucup surucup\n")
    # 'w' bikin baru dan akan menimpa/overwrite
    # 'a' akan menimpa data yang sudah ada

with open("Episode65/data_2.txt", 'a',encoding="utf-8") as file:
    file.write("ojon siojon\n")

with open("Episode65/data_2.txt", 'a',encoding="utf-8") as file:
    file.write("udin sedunia")

# 3. mode r+
with open("Episode65/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("Episode65/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris 1\n")
    file.write("baris 2\n")
    file.write("baris 3\n")

with open("Episode65/data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)
    
with open("Episode65/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("otong") # akan menimpa isi text sesuai dengan panjang data
    
    


