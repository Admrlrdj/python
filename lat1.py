uts = float(input("Masukkan Nilai UTS: "))
utsp = float(input("Masukkan Nilai UTSP: "))
uas = float(input("Masukkan Nilai UAS: "))
uasp = float(input("Masukkan Nilai UASP: "))

hasil_uts = uts * 0.3
hasil_utsp = utsp * 0.15
hasil_uas = uas * 0.4
hasil_uasp = uasp * 0.15
hasil_akhir = hasil_uas + hasil_uasp + hasil_uts + hasil_utsp

if hasil_akhir >= 80:
    print("Nilai Akhir: ", hasil_akhir)
    print("Nilai Mutu: A")
elif hasil_akhir >= 70:
    print("Nilai Akhir: ", hasil_akhir)
    print("Nilai Mutu: B")
elif hasil_akhir >= 60:
    print("Nilai Akhir: ", hasil_akhir)
    print("Nilai Mutu: C")
elif hasil_akhir >= 40:
    print("Nilai Akhir: ", hasil_akhir)
    print("Nilai Mutu: D")
else:
    print("Nilai Akhir: ", hasil_akhir)
    print("Nilai Mutu: E")

# print(hasil_uts)
# print(hasil_utsp)
# print(hasil_uas)
# print(hasil_uasp)
# print(hasil_akhir)

# bil = int(input("Masukkan bilangan: "))

# if bil % 2 == 0 and bil >= 0:
#     print(bil, "Bilangan Genap Positif")
# elif bil % 2 == 0 and bil <= 0:
#     print(bil, "Bilangan Genap Negatif")
# elif bil % 2 == 1 and bil >= 0:
#     print(bil, "Bilangan Ganjil Positif")
# elif bil % 2 == 1 and bil <= 0:
#     print(bil, "Bilangan Ganjil Negatif")

# if bil % 2 == 0:
#     if bil >= 0:
#         print(bil, "Bilangan Genap Positif")
#     else:
#         print(bil, "Bilangan Genap Negatif")
# else:
#     if bil >= 0:
#         print(bil, "Bilangan Ganjil Positif")
#     else:
#         print(bil, "Bilangan Ganjil Negatif")


# if bil>10:
#     print(bil, "lebih besar dari 10")
# elif bil == 10:
#     print(bil, "sama dengan 10")
# else:
#     print(bil, "lebih kecil dari 10")