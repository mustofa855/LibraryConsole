# module matematika dengan import

from matematika import tambah as add
from matematika import kali as kl
from matematika import pangkat as pk
# from matematika import *

import matematika as math

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

hasil_pangkat = pk(3)
print(f"Hasil pangkat 3 = {hasil_pangkat(3)}")
