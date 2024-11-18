nilainilai = []

jumlah = int(input("Mau masukin berapa nilai? "))


for i in range(jumlah):
    nilai = float(input("Masukan nilai nilai:\n"))
    nilainilai.append(nilai)
    print(i)

ratarata = (sum(nilainilai)) / jumlah if jumlah > 0 else 0

print("Daftar nilai", nilainilai)
print(f"ratarata : \n {ratarata}")
