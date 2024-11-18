buahbuah = []

jumlah = int(input("Mau nambahin berapa kali?"))

for i in range(jumlah):
    buah = str(input("Masukkan nama nama buah :\n"))
    buahbuah.append(buah)
    if i == jumlah-1:
        keputusan = input("Mau ngehapus data ngga?[Y/n]\n")
        if keputusan == "Y" or keputusan == "y":
            mauHapus = str(input("yang mana mau hapus?"))
            if mauHapus in buahbuah:
                buahbuah.remove(mauHapus)
                print(f"Data {mauHapus} sudah dihapus")
            else:
                print(f"Data {mauHapus} ngga ada")
        else:
            pass

print(buahbuah)

        