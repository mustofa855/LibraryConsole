'''Fungsi dengan argumen (input)'''

# template
'''
    def nama_fungsi(argument):
        badan fungsi
'''

def hello_world(nama):
    '''fungsi hello world menerima input variabel nama'''
    print(f"Selamat datang wahai {nama}")

hello_world("ucup")
hello_world("Asep")


# program tambah

def tambah(angka1,angka2):
    '''Fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5)
tambah(7,5)

def say_hay(list_peserta):
    '''Ini adalah fungsi say hi'''
    list_peserta[1] = "asep kasep"
    dataPeserta = list_peserta.copy()
    for peserta in dataPeserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["ucup","otong","dudung"]
say_hay(anggota_boyband)
print(anggota_boyband[1])
