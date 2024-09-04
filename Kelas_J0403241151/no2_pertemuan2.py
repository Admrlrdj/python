def max_min_3_ints(a, b, c):
    # Menentukan bilangan terbesar dan terkecil
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    return max_num, min_num

while True:
    # Contoh penggunaan dengan input dari pengguna
    bil1 = int(input("Masukkan bilangan pertama: "))
    bil2 = int(input("Masukkan bilangan kedua: "))
    bil3 = int(input("Masukkan bilangan ketiga: "))

    max_num, min_num = max_min_3_ints(bil1, bil2, bil3)
    print("Bilangan terbesar:", max_num)
    print("Bilangan terkecil:", min_num)
    # Meminta pengguna untuk melanjutkan atau berhenti
    lanjut = input("Apakah Anda ingin menjumlahkan lagi? (y/n): ").lower()
    if lanjut != 'y':
        break
