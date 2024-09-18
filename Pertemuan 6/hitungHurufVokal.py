teks = input("Masukkan teks: ")
vokal = 'aiueoAIUEO'
jumlah_vokal = 0

for char in teks:
    if char in vokal:
        jumlah_vokal += 1

print("Jumlah huruf vokal:", jumlah_vokal)