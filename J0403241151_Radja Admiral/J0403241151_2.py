bil = int(input())

if bil % 2 == 1:
    if bil > 0:
        print(bil)
    else:
        print(bil , "bukan bilangan bulat ganjil positif")
else:
    print(bil , "bukan bilangan bulat ganjil positif")