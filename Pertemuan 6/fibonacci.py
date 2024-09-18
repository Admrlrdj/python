jumlahFibonacci = int(input("Masukkan angka: "))

# a, b = 0, 1
# print("Deret Fibonacci:")
# for i in range(jumlahFibonacci):
#     print(a, end=" ")
#     a, b = b, a + b

a, b = 1, 1
print("Deret Fibonacci:")

for i in range(jumlahFibonacci):
    if a > jumlahFibonacci:
        break
    print(a, end=" ")
    a, b = b, a + b