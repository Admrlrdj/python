def find_remainder(number, x):
    if x > 0:
        return number % x
    else:
        return "x harus lebih besar dari 0."

# Contoh penggunaan dengan input dari pengguna
number = int(input("Masukkan bilangan bulat: "))
x = int(input("Masukkan nilai modulus "))

remainder = find_remainder(number, x)
print("Sisa pembagian adalah:", remainder)
