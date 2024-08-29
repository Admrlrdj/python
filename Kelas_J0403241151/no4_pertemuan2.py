import math

def luas_lingkaran():
    jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * (jari ** 2)
    return luas

def luas_bujur_sangkar():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    return luas

def luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    return luas

while True:
    print("\nPilih bentuk untuk menghitung luas:")
    print("1. Lingkaran")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == '1':
        luas = luas_lingkaran()
        print(f"Luas Lingkaran: {luas:.2f}")
        input()
    elif pilihan == '2':
        luas = luas_bujur_sangkar()
        print(f"Luas Persegi: {luas:.2f}")
        input()
    elif pilihan == '3':
        luas = luas_segitiga()
        print(f"Luas Segitiga: {luas:.2f}")
        input()
    elif pilihan == '4':
        break
