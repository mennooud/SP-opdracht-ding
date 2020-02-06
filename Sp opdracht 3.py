
lijstje = [1, 2, 6, 3, 34, 5, 1, 3, 5, 9]
a = input('Getal')
def count(lijstje, a):
    b = 0
    for i in lijstje:
        if int(a) == i:
            b += 1
    return b


print("Dit getal komt " + str(count(lijstje, a)) + " keer voor")



def verschil(lijstje):
    i = 0
    m = 0
    while i != (len(lijstje)-1):
        n = lijstje[i] - lijstje[i+1]
        if n < 0:
            n = n*-1
        if n > m:
            m = n
        i += 1
    print(m)

verschil(lijstje)

lijst = [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
def functie(lijst):
    x = count(lijst, 0)
    if x > 12:
        return(0)
    else:
        y = count(lijstje, 1)
        if y < x:
            return(1)
        else:
            return(2)

print(functie(lijst))