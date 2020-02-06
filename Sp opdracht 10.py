a = int(input("Geef een Fibonaci getal: "))
b = 0
c = [0, 1]
def Fibonaci(FibonaciA, Rotatie, Lijst):
    if FibonaciA == Rotatie:
        print(Lijst[0])
    else:
        Tel = Lijst[0] + Lijst[1]
        Lijst[0] = Lijst[1]
        Lijst[1] = Tel
        Rotatie += 1
        Fibonaci(FibonaciA, Rotatie, Lijst)



Fibonaci(a, b, c)