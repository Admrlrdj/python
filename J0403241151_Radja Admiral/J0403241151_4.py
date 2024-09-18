suhu = int(input())

if suhu < 0:
    print("dingin sekali")
elif suhu >= 0 and suhu <= 20:
    print("dingin")
elif suhu > 20 and suhu <= 30:
    print("hangat")
else:
    print("panas")