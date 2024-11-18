# Program untuk menghitung operasi logika AND, OR, dan NOT pada dua nilai boolean

# Meminta input boolean dari pengguna
# Input akan dikonversi menjadi boolean, misalnya input "True" atau "False"
nilai1 = input("Masukkan nilai boolean pertama (True/False): ").capitalize()
nilai2 = input("Masukkan nilai boolean kedua (True/False): ").capitalize()

# Konversi input menjadi boolean
nilai1 = True if nilai1 == "True" else False
nilai2 = True if nilai2 == "True" else False

# Operasi logika AND, OR, dan NOT
hasil_and = nilai1 and nilai2
hasil_or = nilai1 or nilai2
hasil_not_nilai1 = not nilai1
hasil_not_nilai2 = not nilai2

# Menampilkan hasil operasi
print(f"\nHasil operasi logika:")
print(f"{nilai1} AND {nilai2} = {hasil_and}")
print(f"{nilai1} OR {nilai2} = {hasil_or}")
print(f"NOT {nilai1} = {hasil_not_nilai1}")
print(f"NOT {nilai2} = {hasil_not_nilai2}")
