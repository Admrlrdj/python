def sum_4_ints():
    while True:
        # Meminta pengguna memasukkan empat bilangan bulat
        bil1 = int(input("Masukkan bilangan pertama: "))
        bil2 = int(input("Masukkan bilangan kedua: "))
        bil3 = int(input("Masukkan bilangan ketiga: "))
        bil4 = int(input("Masukkan bilangan keempat: "))
        
        # Menjumlahkan keempat bilangan
        result = bil1 + bil2 + bil3 + bil4
        print("Hasil dari penjumlahan 4 bilangan:", result)
        
        # Meminta pengguna untuk melanjutkan atau berhenti
        lanjut = input("Apakah Anda ingin menjumlahkan lagi? (y/n): ").lower()
        if lanjut != 'y':
            break

# Memanggil fungsi
sum_4_ints()
