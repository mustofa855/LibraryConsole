# Latihan konversi satuan temperatur

# progran konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR CELCIUS KE SATUAN LAIN\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ", celcius, 'C')

# reamur
# 4/5.C
reamur  = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, 'R')

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, 'F')

# Kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin adalah ", kelvin, 'F')


# progran konversi farenheit ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR FAHRENHEIT KE SATUAN LAIN\n")

fahrenheit = float(input('Masukkan suhu dalam Fahrenheit : '))
print("suhu adalah ", fahrenheit, 'F')

# reamur
# 4/5.C
reamur  = ((4/9) * (fahrenheit-32))
print("suhu dalam reamur adalah ", reamur, 'R')

# celcius
celcius = ((5/9) * (fahrenheit - 32))
print("suhu dalam celcius adalah ", celcius, 'C')

# Kelvin
kelvin = (fahrenheit + 459) * (5/9)
print("suhu dalam Kelvin adalah ", kelvin, 'K')

# progran konversi Kelvin ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR KELVIN KE SATUAN LAIN\n")

kelvin = float(input('Masukkan suhu dalam Kelvin : '))
print("suhu adalah ", kelvin, 'K')

# reamur
reamur  = ((4/5) * (kelvin-273))
print("suhu dalam reamur adalah ", reamur, 'R')

# celcius
celcius = (kelvin - 273)
print("suhu dalam celcius adalah ", celcius, 'C')

# Fahrenheit
fahrenheit = ((9/5) * (kelvin - 273) + 32)
print("suhu dalam fahrenheit adalah ", fahrenheit, 'F')