a = int(input("Masukkan panjang sisi pertama (a): "))
b = int(input("Masukkan panjang sisi kedua (b): "))
c = int(input("Masukkan panjang sisi ketiga (c): "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga tersebut adalah segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga tersebut adalah segitiga sama kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Sisi-sisi tersebut tidak bisa membentuk segitiga")