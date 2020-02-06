b = input("Geef woord")

def palindroom(a):
    c = ''.join(reversed(a))
    if a == c:
        return 1
    else:
        return 0

def palinzelf(a):
    c = a[::-1]
    if a == c:
        return 1
    else:
        return 0

print(palindroom(b))
print(palinzelf(b))