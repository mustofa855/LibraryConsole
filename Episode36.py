# Program List Buku

list_buku = []
while True:
    print("Masukkan data buku")
    judul = input("judul buku : \t")
    penulis = input("nama penulis : \t")

    buku_baru =[judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10)
    print("No.\t| Judul\t\t| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index}\t|{buku[0]}\t\t| {buku[1]}")
    
    print("\n\n","="*10)
    isLanjut = input("apakah lanjutkan?Y/n\n")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")

    





