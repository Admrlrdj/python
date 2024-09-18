tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir (dalam angka): "))

if tanggal >= 21 and bulan == 3 or tanggal <= 19 and bulan == 4:
    zodiak = "Aries"
elif tanggal >= 20 and bulan == 4 or tanggal <= 20 and bulan == 5:
    zodiak = "Taurus"
elif tanggal >= 21 and bulan == 5 or tanggal <= 20 and bulan == 6:
    zodiak = "Gemini"
elif tanggal >= 21 and bulan == 6 or tanggal <= 22 and bulan == 7:
    zodiak = "Cancer"
elif tanggal >= 23 and bulan == 7 or tanggal <= 22 and bulan == 8:
    zodiak = "Leo"
elif tanggal >= 23 and bulan == 8 or tanggal <= 22 and bulan == 9:
    zodiak = "Virgo"
elif tanggal >= 23 and bulan == 9 or tanggal <= 22 and bulan == 10:
    zodiak = "Libra"
elif tanggal >= 23 and bulan == 10 or tanggal <= 21 and bulan == 11:
    zodiak = "Scorpio"
elif tanggal >= 22 and bulan == 11 or tanggal <= 21 and bulan == 12:
    zodiak = "Sagittarius"
elif tanggal >= 22 and bulan == 12 or tanggal <= 19 and bulan == 1:
    zodiak = "Capricorn"
elif tanggal >= 20 and bulan == 1 or tanggal <= 18 and bulan == 2:
    zodiak = "Aquarius"
elif tanggal >= 19 and bulan == 2 or tanggal <= 20 and bulan == 3:
    zodiak = "Pisces"
else:
    zodiak = "Zodiak tidak valid"

print("Zodiak Anda adalah", zodiak)

#################################################################################

# tanggal = int(input("Masukkan tanggal lahir: "))
# bulan = int(input("Masukkan bulan lahir (dalam angka): "))

# if bulan == 3:
#     if tanggal >= 21:
#         zodiak = "Aries"
#     else:
#         zodiak = "Pisces"
# elif bulan == 4:
#     if tanggal <= 19:
#         zodiak = "Aries"
#     else:
#         zodiak = "Taurus"
# elif bulan == 5:
#     if tanggal <= 20:
#         zodiak = "Taurus"
#     else:
#         zodiak = "Gemini"
# elif bulan == 6:
#     if tanggal <= 20:
#         zodiak = "Gemini"
#     else:
#         zodiak = "Cancer"
# elif bulan == 7:
#     if tanggal <= 22:
#         zodiak = "Cancer"
#     else:
#         zodiak = "Leo"
# elif bulan == 8:
#     if tanggal <= 22:
#         zodiak = "Leo"
#     else:
#         zodiak = "Virgo"
# elif bulan == 9:
#     if tanggal <= 22:
#         zodiak = "Virgo"
#     else:
#         zodiak = "Libra"
# elif bulan == 10:
#     if tanggal <= 22:
#         zodiak = "Libra"
#     else:
#         zodiak = "Scorpio"
# elif bulan == 11:
#     if tanggal <= 21:
#         zodiak = "Scorpio"
#     else:
#         zodiak = "Sagittarius"
# elif bulan == 12:
#     if tanggal <= 21:
#         zodiak = "Sagittarius"
#     else:
#         zodiak = "Capricorn"
# elif bulan == 1:
#     if tanggal <= 19:
#         zodiak = "Capricorn"
#     else:
#         zodiak = "Aquarius"
# elif bulan == 2:
#     if tanggal <= 18:
#         zodiak = "Aquarius"
#     else:
#         zodiak = "Pisces"
# else:
#     zodiak = "Tanggal atau bulan tidak valid"

# print("Zodiak Anda adalah", zodiak)