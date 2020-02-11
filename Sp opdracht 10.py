def vraag():
    a = int(input("Geef een Fibonaci getal: "))
    b = 0
    c = [0, 1]
    Fibonaci(a, b, c)
def Fibonaci(FibonaciA, Rotatie, Lijst):
    if FibonaciA == Rotatie:
        print(Lijst[0])
    else:
        Lijst[0], Lijst[1] = Lijst[1], Lijst[0] + Lijst[1]
        Rotatie += 1
        Fibonaci(FibonaciA, Rotatie, Lijst)

vraag()