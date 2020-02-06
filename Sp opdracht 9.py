a = input("Geef een string ")
b = int(input("Geef een rotatie "))
def Cyclish(CH, N):
    d = ""
    for character in CH:
        c = (bin(ord(character))[2:].zfill(8))
        c = (c[N:]) + (c[:N])
        d = d + c + " "
    return d
print(Cyclish(a, b))