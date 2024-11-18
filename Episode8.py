# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'x',b,'=',hasil)

# operasi pembagian /
hasil = a * b
print(a,'x',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'x',b,'=',hasil)

# operasi modulus (sisa bagi) %
hasil = a % b
print(a,'x',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'x',b,'=',hasil)

# Prioritas operasi, operational prersedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,'+',x,'/',y,'-',y,'%',z,'//',x,' = ', hasil)

# prioritas 1 -> ()
# prioritas 2 -> exponen **
# prioritas 3 -> perkalian *
# prioritas 4 -> pertambahan + dan pengurangan -

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)