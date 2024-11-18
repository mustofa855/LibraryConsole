# a = 10, a adalah variabel dengan nilai 10

# tipe data angka satuan (integer)
data_integer = 1
print(type(data_integer))
print("data : ", data_integer, "bertipe", type(data_integer))


# tipe data desimal/float(angka dengan koma)
data_float = 1.5
print(type(data_float))
print("data : ", data_float, "bertipe", type(data_float))

# tipe data string(kumpulan karakter)
data_string = "ucup"
print(type(data_string))
print("data : ", data_string, "bertipe", type(data_string))

# tipe data bool(kumpulan karakter)
data_bool = True
print(type(data_bool))
print("data : ", data_bool, "bertipe", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_kompleks = complex(5,6)
print("data : ", data_kompleks)
print("- bertipe : ", type(data_kompleks))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-Bertipe : ", type(data_c_double))

