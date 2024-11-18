# format string

# contoh generic

# string
print(10*"=-")
nama = "merlene"
format_str = f"hello {nama}"
print(format_str)

# boolean
print(10*"=-")
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
print(10*"--")
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
print(10*"--")
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
print(10*"--")
angka = 2000000
format_str = f"ribuan bulat = {angka:,}"
print(format_str)

# bilangan desimal
print(10*"--")
angka = 2005.54321
format_str = f"bilangan desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
print(10*"--")
angka = 2005.54321
format_str = f"bilangan desimal = {angka:8.2f}"
print(format_str)

# menampilkan +/-
print(10*"--","menampilkan +/-")
angka_minus = -10
angka_plus = +10.12345
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.3f}"
print(format_minus)
print(format_plus)

# memformat %
print(10*"--","memformat persen %")
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
print(10*"--","melakukan operasi aritmatika")
harga = 10000
jumlah = 5

format_string = f"harga_total = {harga*jumlah:,}"
print(format_string)

# format angka lain
print(10*"--","format angka lain")
angka = 255
format_binary = f"binary = {bin(angka)}" 
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

