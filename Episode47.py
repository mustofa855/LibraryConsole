'''Default Argument'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh 1

def say_hello(nama = "Kasep"):
    '''Fungsi dengam default argument'''
    print(f"Halo {nama}")

say_hello("jalu")
say_hello()

# contoh 2

def sapa_dia(nama,pesan = "apa kabar"):
    '''Fungsi dengan satu input biasa dan satu default argumen'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Hai ganteng", "dudung")
sapa_dia("Jalu")

# contoh 3

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(angka=5,pangkat=2)
print(hasil)

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))


