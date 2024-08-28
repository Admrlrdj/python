# Memasukkan 2 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Salah satu bilangan adalah 5
if a == 5 or b == 5:
    print(True)
# Jumlah kedua bilangan adalah 5
elif a + b == 5:
    print(True)
# Selisih kedua bilangan adalah 5
elif abs(a - b) == 5:
    print(True)
# Tidak memenuhi kriteria
else:
    print(False)