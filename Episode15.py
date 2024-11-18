# Pengenalan String
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. Dengan menggunakan single quote -> '...'
    2. Dengan menggunakan double quote -> "..." 
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo apa kabar semuanya??"')
print("'Halo apa kabar semuanya??'")
print("ini adalah hari jum'at")

# 2. menggunakan back slash

# membuat tanda ini ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# back slash
print("C:\\user\\ucup")

# tab
print("ucup\totong") #bikin tab diantara ucup dan otong

# backspace
print("ucup\botong") #menghapus huruf sebelum \b

# newline
print("baris pertama.\nbaris kedua.") # LF line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF line feed carriage return -> dipakai oleh windows


# 3. String literal atau raw

# hati-hati
print('C:\new folder')

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD \new normal
website : www.ucup.com/ucupid
""")