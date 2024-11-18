# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++++++3-------------10+++++++++

inputUser = float(input("masukkan angka yang bernilai kurang dari 3 atau lebih dari 10 : "))

# +++++++3---------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ",isKurangDari)

# --------------10+++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

print(40*"=") # garis batas

# -----3+++++++++10--------
# kasus irisan
inputUser = float(input("masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 : "))

# ----3++++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 = ', isLebihDari)

# +++++++++++++++++10----
# kurang dari 10
isKurangDari = inputUser < 10
print('Kurang dari 3 = ', isKurangDari)

# --------3++++true++++++10-----------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)


# TUGAS
print(10*'>','Tugas',10*'<')# garis batas

inputUser = float(input("masukkan angka yang bernilai lebih dari 0 dan kurang dari 5 dan lebih dari 8 dan kurang dari 11 : "))

# lebih dari 0
isLebihDari1 = inputUser > 0
print('Lebih dari 0 = ', isLebihDari1)

# kurang dari 5
isKurangDari1 = inputUser < 5
print('Kurang dari 5 = ', isKurangDari1)

# lebih dari 8
isLebihDari2 = inputUser < 8
print('Kurang dari 8 = ', isLebihDari2)

# kurang dari 11
isKurangDari2 = inputUser < 11
print('Kurang dari 11 = ', isKurangDari2)

# --------0++++5----8++++++11-----------
isCorrect = isKurangDari1 and isLebihDari1 and isKurangDari2 and isLebihDari2
print("angka yang anda masukkan: ", isCorrect)



