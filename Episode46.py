'''Fungsi dengan kembalian (return)'''

# template fungsi dengan kembalian]
# def nama_fungsi(argument):
#   badan fungsi
#   return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat
y = kuadrat(9)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka1,angka2):
    '''Fungsi return dengan multi input'''
    return angka1 + angka2

a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak
def operasi_mtk(angka1,angka2):
    kali = angka1 * angka2
    bagi = angka1 / angka2
    tambah = angka1 + angka2
    kurang = angka1 - angka2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_mtk(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")
 