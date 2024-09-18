N = int(input())

romawi_nilai = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

hasil_romawi = ""

for nilai, simbol in romawi_nilai:
    while N >= nilai:
        hasil_romawi += simbol 
        N -= nilai              

# Tampilkan hasil
print(hasil_romawi)

