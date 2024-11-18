# IF dan ELSE Statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("siapa nama anda?? :")
print(nama)

# cara nulis kode
# if kondisi(boolean): 
#    aksi

# program selanjutnya

# if inline
# if nama == "ucup" : print(nama+" kamu ganteng")
# print(f"terima kasih{nama}")


# if indentatation
print(5*"^v"+"IF INDENTATION"+"^v"*5)
if nama == "ucup":
    print("kamu ganteng banget")
    print("kamu juga keren banget")
print(f"terima kasih {nama}")

# else statement
print(5*"^v"+"ELSE STATEMENT"+"^v"*5)
if nama == "otong":
    print("hai otong, si keren")
else:
    print("kamu bukan otong")
print(f"Terima kasih{nama}")