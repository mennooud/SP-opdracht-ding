
lijstje = [1, 2, 6, 3, 34, 5, 1, 3, 5, 9]

def count(lijstje):
    a = input('Getal')
    b = 0
    for i in lijstje:
        if int(a) == i:
            b += 1
    print("Dit getal komt " +b+" keer voor")
count(lijstje)