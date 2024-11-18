# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aiueoAIUEO"

# Menghitung jumlah huruf vokal dalam kalimat
jumlah_vokal = 0
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat adalah: {jumlah_vokal}")
