# import

# fungsinya adalah untuk mengambil program dari file external .py

# 1 - untuk menyambung progran daru external
import print_app
import ucup_app

# 2. import dengan data
import variable
import kucuy

# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)
