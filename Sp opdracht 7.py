import random
a = random.randint(1, 10)
def gok(a):
    b = int(input("Getal "))
    if b != a:
        gok(a)
    else:
        print("Goed")
gok(a)