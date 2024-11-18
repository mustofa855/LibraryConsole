"""
    Buat program Python yang mendeklarasikan 3 variabel 
    dengan tipe data berbeda (string, integer, dan float). 
    Ubah tipe data masing-masing variabel 
    menggunakan casting.
"""

# Mendekalrasikan variabel dengan tipe data berbeda
nama = "Asep"    # Tipe data string
umur = 25        # Tipe data integer
tinggi = 175.5   # Tipe data float

# Menampilkan tipe data awal
print("tipe data awal: ")
print("nama: ", type(nama))
print("umur: ", type(umur))
print("tinggi: ", type(tinggi))

# casting tipe data
tinggi = int(tinggi)
umur = str(umur)

# menampilkan hasil setelah casting
print("\nSetelah casting")
print("nama", nama,type(nama))
print("tinggi", tinggi,type(tinggi))
print("umur", umur,type(umur))
