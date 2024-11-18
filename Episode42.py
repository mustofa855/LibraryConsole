import datetime

# Data mahasiswa
mahasiswa1 = {
    "nama": "ucup surucup",
    "nim": "203040030",
    "sks_lulus": 140,
    "beasiswa": False,
    "lahir": datetime.datetime(2002, 2, 22),
}

mahasiswa2 = {
    "nama": "otong surotong",
    "nim": "193040030",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2002, 2, 22),
}

mahasiswa3 = {
    "nama": "asep suratep",
    "nim": "213040030",
    "sks_lulus": 140,
    "beasiswa": False,
    "lahir": datetime.datetime(2002, 2, 22),
}

mahasiswa4 = {
    "nama": "madara uchiha",
    "nim": "223040030",
    "sks_lulus": 140,
    "beasiswa": False,
    "lahir": datetime.datetime(2002, 2, 22),
}

mahasiswa5 = {
    "nama": "mugen",
    "nim": "233040030",
    "sks_lulus": 140,
    "beasiswa": False,
    "lahir": datetime.datetime(2002, 2, 22),
}

data_mhs = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
    'MAH004': mahasiswa4,
    'MAH005': mahasiswa5
}

# Header tabel
print(f"{'KEY':<8} {'Nama':<15} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mhs:
    KEY = mahasiswa

    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs [KEY]['nim']
    SKS = data_mhs [KEY]['sks_lulus']
    BEASISWA = data_mhs [KEY]['beasiswa']
    LAHIR = data_mhs [KEY]['lahir'].strftime("%x")

    print(f"{KEY:<8} {NAMA:<15} {SKS:<5} {BEASISWA:^ 9} {LAHIR:<10}")





