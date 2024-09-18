berat_paket = float(input())
jenis_layanan = input()

#* RINGAN
if berat_paket <= 1:
    #! EKONOMI
    if jenis_layanan == "E" or "e":
        # print("ringan + ekonomi")
        print(10000)
    #! STANDAR
    elif jenis_layanan == "S" or "s":
        # print("ringan + standar")
        print(15000)
    #! EKSPRES
    elif jenis_layanan == "X" or "x":
        # print("ringan + ekspres")
        print(25000)
#* SEDANG
elif berat_paket <= 5:
    #! EKONOMI
    if jenis_layanan == "E" or "e":
        # print("sedang + ekonomi")
        print(20000)
    #! STANDAR
    elif jenis_layanan == "S" or "s":
        # print("sedang + standar")
        print(25000)
    #! EKSPRES
    elif jenis_layanan == "X" or "x":
        # print("sedang + ekspres")
        print(40000)
#* BERAT
else:
    #! EKONOMI
    if jenis_layanan == "E" or "e":
        # print("berat + ekonomi")
        print(30000)
    #! STANDAR
    elif jenis_layanan == "S" or "s":
        # print("berat + standar")
        print(35000)
    #! EKSPRES
    elif jenis_layanan == "X" or "x":
        # print("berat + ekspres")
        print(50000)
