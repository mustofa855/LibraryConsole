# Break
angka = 0

while angka < 5:
    angka += 1
    print(f"count = {angka}")

    if angka == 3:
        print("nice!")
        break

    print("wassup!")

print("cukup finish")

# kedua
data_int = int(input("hitung sampai berapa = "))
angka = 0
while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("nice!")
        break

    print("wassup!")

print("cukup finish")
