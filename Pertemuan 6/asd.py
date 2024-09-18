list_a = [10, 2, 7, 4, 5]

i = 0
while i<len(list_a):
    if(list_a[i]%2 == 0):
        list_a[i] = "genap"
        print("genap", end=" ")
    else:
        print(list_a[i], end=" ")
    i += 1

# print(list_a)