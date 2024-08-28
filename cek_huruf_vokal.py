def cek_huruf_vokal(teks):
    vokal = "aiueoAIUEO" #Huruf Vokal
    hasil = {} #Array untuk menyimpan hasil
    for huruf in teks:
        if huruf in vokal:
            hasil[huruf] = hasil.get(huruf, 0) + 1
    return hasil

teks_input = input("Masukkan Teks: ")
output_vokal = cek_huruf_vokal(teks_input)

if output_vokal:
    print (teks_input)
    print("Huruf vokal yang ditemukan beserta jumlahnya: ")
    for huruf, jumlah in output_vokal.items():
        print(f"{huruf}: {jumlah}")
else:
    print("Huruf vokal tidak ditemukan")