from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_buku):
    try:
        # Hapus data_temp.txt jika ada
        if os.path.exists("data_temp.txt"):
            os.remove("data_temp.txt")

        with open(Database.DB_NAME, 'r') as file:
            counter = 0

            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass  # Skip the line that needs to be deleted
                else:
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1

        # Pastikan data.txt tidak ada sebelum mengganti nama
        if os.path.exists(Database.DB_NAME):
            os.remove(Database.DB_NAME)

        # Ganti nama file sementara menjadi file utama
        os.rename("data_temp.txt", Database.DB_NAME)
    except Exception as e:
        print(f"Error: {e}")

def update(no_buku, pk, data_add, tahun, judul, penulis):
    try:
        # Baca seluruh file
        with open(Database.DB_NAME, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Menyiapkan data baru
        data = Database.TEMPLATE.copy()
        data["pk"] = pk
        data["date_add"] = data_add
        data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data["tahun"] = str(tahun)
        
        # Format data menjadi satu baris CSV
        data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

        # Update baris yang sesuai
        lines[no_buku - 1] = data_str  # No buku - 1 karena indeks mulai dari 0

        # Tulis ulang file dengan data yang sudah diperbarui
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.writelines(lines)

    except Exception as e:
        print(f"Error dalam update data: {e}")


def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:    
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    