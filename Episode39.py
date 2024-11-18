# operator dalam dictionary

data_dict ={
    'cups':"ucup",
    'tong':'otong',
    'dung':'udung'
}

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary: {lendict}")

# mengecek key exist atau tidak
KEY = "cups"
CHEKKEY = KEY in data_dict
print(f"data {KEY} ada di data_dict: {CHEKKEY}")

# mengakses value dengan get
print(data_dict["cups"])
print(data_dict.get("cups"))
print(data_dict.get("mad","key tidak ditemukan"))

# mengupdate data
data_dict["cups"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"cups":"ucup surucup"})
print(data_dict)
data_dict.update({"muss":"mus ganteng"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["muss"]
print(data_dict)
