try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid, harap masukkan angka.")
    exit()
print(angka)