"""
    Buat program yang meminta pengguna memasukkan dua angka, 
    lalu bandingkan angka tersebut menggunakan operator 
    komparasi dan tampilkan hasilnya (lebih besar, 
    lebih kecil, atau sama).
"""

print("pembandingan")
angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))

print(f"Apakah {angka1} dengan {angka2} lebih besar?lebih kecil? atau sama??")

if angka1 == angka2:
    print(f"{angka1} SAMA DENGAN {angka2}")
elif angka1 < angka2:
    print(f"{angka1} KURANG DARI {angka2}")
elif angka1 > angka2:
    print(f"{angka1} LEBIH DARI {angka2}")