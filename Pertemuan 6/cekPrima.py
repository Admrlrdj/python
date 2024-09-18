angka = int(input("Masukkan bilangan: "))

# print("Bilangan prima:")
# for bil in range(2, maxBil + 1):
#     prima = True
#     for i in range(2, int(bil**0.5) + 1):
#         if bil % i == 0:
#             prima = False
#             break
#     if prima:
#         print(bil, end=" ")

if angka <= 1:
    print(angka, "bukan bilangan prima")
else:
    prima = True
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            prima = False
            break
    if prima:
        print(angka, "adalah bilangan prima")
    else:
        print(angka, "bukan bilangan prima")