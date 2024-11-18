import datetime
import os

os.system('cls')

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun now : {data_waktu.year}")
print(f"tahun now : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","d","e"]

data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")

import io

file = io.open("episode58/file.txt","r")
print(file.read())