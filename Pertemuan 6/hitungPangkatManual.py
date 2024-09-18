angka = int(input("Masukkan angka: "))
pangkat = int(input("Masukkan pangkat: "))

hasil = 1
hitung = 0
while hitung < pangkat:
    hasil *= angka
    hitung += 1

print(angka, "pangkat", pangkat, "adalah", hasil)