kalimat = str(input("Masukkan kalimat anda :\n"))

kapital = kalimat
lower = kapital
judul = kapital
balik = kalimat

print("Ini adalah hasil perubahan : ",kapital.upper())
print("Ini adalah hasil perubahan : ",lower.lower())
print("Ini adalah hasil perubahan : ",judul.title())
print("Ini adalah hasil perubahan : ",balik[::-1])
print("Panjang string : ",len(kalimat))
