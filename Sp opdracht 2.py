def Sp_Opdracht_2():
    i = 0
    c = 0
    a = input("Geef tekst")
    b = input("Geef meer tekst")
    while i != len(a) and i != len(b):
        if a[i] == b[i]:
            c += 1
            i += 1
        else:
            break
    print("Je eerste index verschil zit op " + str(c))

print("baguette")
Sp_Opdracht_2()