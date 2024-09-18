kata = input("Masukkan kata: ")
vokal = "aiueoAIUEO"
hasil = ""

for huruf in kata:
    if huruf in vokal:
        hasil += "i"
    else:
        hasil += huruf

print(hasil)
