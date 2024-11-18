## tutorial membaca file eksternal

print(5*"="," Membaca File TXT ", 5*"=")

file = open("Episode64/data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
print(file.read())

# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua

## Baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

## salah satu tehnik membuka file di python
print("\n",5*"="," Membaca file txt dengan with ",5*"=")

with open("Episode64/data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")
print(f"apakah file sudah diclose : {file.closed}")