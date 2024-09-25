angka = int(input("Masukkan angka: "))

ketemu = False

for i in range(2, angka):
    prima1 = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prima1 = False
            break
    
    prima2 = True
    for j in range(2, int((angka - i)**0.5) + 1):
        if (angka - i) % j == 0:
            prima2 = False
            break
    
    if prima1 and prima2:
        print("Iya,", i, "dan", angka - i, "adalah Prima")
        ketemu = True
        break
    
if not ketemu:
    print("Tidak, tidak ada pasangan bilangan prima yang jika dijumlahkan menghasilkan", angka)
