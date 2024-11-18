# continue, pass, break

# pass 
# berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka < 5:
#     angka+=1
#     if angka == 3:
#         print("whatsapp!")
#         pass # ini tidak akan dieksekusi

#     print(angka)

# continue

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1

    if angka == 3:
        print("nice bro")
        continue # akan meloncat ke step selanjutnya

    print("whatsapp") #aksi 2
    # apapun yang dibawah continue akan diskip

print("finish")