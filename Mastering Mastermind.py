import random

def start():
    wie = input("Wil je zelf gokken of de pc laten gokken?").lower()
    if wie == ("pc"):
        print("Not yet")
    else:
        if wie == ("zelf"):
            randomcode()
        else:
            start()

def randomcode():
    code = []
    while len(code) != 4:
        randomkleur = random.randint(1, 6)
        if randomkleur == 1:
            code.append("wit")
        else:
            if randomkleur == 2:
                code.append("zwart")
            else:
                if randomkleur == 3:
                    code.append("rood")
                else:
                    if randomkleur == 4:
                        code.append("blauw")
                    else:
                        if randomkleur == 5:
                            code.append("geel")
                        else:
                            code.append("groen")
    print(code)
    gok(code)

def gok(code):
    mode = input("Easy of normal?").lower()
    poging = 1
    while poging != 11:
        print("Je hebt hiervoor nog " + str(11 - poging) + " pogingen")
        if poging == 10:
            print("Laatste kans")
        hint = []
        gok = []
        b = len(gok)
        while b != 3:
            b = len(gok)
            gok.append(input("Gok kleur "+ str(b+1) + ": "))
        if gok == code:
            print("Gefeliciteerd")
            break
        else:
            c = len(hint)
            while c != 3:
                c = len(hint)
                if code[c] == gok[c].lower():
                    hint.append("zwarte pin")
                else:
                    if gok[c] in code:
                        hint.append("witte pin")
                    else:
                        hint.append("geen pin")

            if mode == ('easy'):
                print(hint)
            else:
                random.shuffle(hint)
                print(hint)
            poging += 1
    start()







start()