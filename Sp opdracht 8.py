a = open("Tekst.txt", 'r')
b = a.readlines()
c = open("Ook tekst.txt", 'w')

for i in b:
    if i != '\n':
        c.write((i.strip() + "\n"))