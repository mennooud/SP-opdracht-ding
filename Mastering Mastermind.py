import random

def start():
    wie = input("Wil je zelf gokken of de pc laten gokken?: ").lower()
    if wie == ("pc"):
        menscode()
    else:
        if wie == ("zelf"):
            randomcode()
        else:
            start()


def randomcode():
    code = []
    while len(code) != 4:
        randomkleur = random.randint(1, 6)
        kleurdict = {1 : "wit", 2 : "zwart", 3 : "rood", 4 : "blauw", 5 : "geel", 6 : "groen"}
        code.append(kleurdict[randomkleur])
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
        gebruikt = []
        b = len(gok)
        zwartepin = 0
        wittepin = 0
        aanpascode = code
        while b != 3:
            b = len(gok)
            gok.append(input("Gok kleur "+ str(b+1) + ": "))
        if gok == code:
            print("Gefeliciteerd")
            break
        else:
            while zwartepin != 3:
                if aanpascode[zwartepin] == gok[zwartepin].lower():
                    aanpascode[zwartepin] = 'gebruikt'
                    hint.append('zwarte pin')
                zwartepin += 1
            while wittepin != 3:
                if gok[wittepin] in aanpascode:
                    aanpas = int(aanpascode.index(gok[wittepin]))
                    aanpascode[aanpas] = 'gebruikt'
                    hint.append('witte pin')
                wittepin += 1
            if len(hint) < 4:
                aantalleeg = 4 - len(hint)
                while aantalleeg > 0:
                    hint.append('geen pin')
                    aantalleeg -= 1


            if mode == ('easy'):
                print(hint)
            else:
                random.shuffle(hint)
                print(hint)
            poging += 1
    start()

def menscode():
    botcode = []
    b = len(botcode)
    while b != 3:
        b = len(botcode)
        kleur = (input("Wat is code kleur " + str(b + 1) + "?: "))
        kleurdict = {'wit' : 1, 'zwart' : 2, "rood" : 3, "blauw" : 4, "geel" : 5, "groen" : 6}
        try:
            botcode.append(kleurdict[kleur])
        except KeyError:
            print("Deze kleur zit niet in de game")
    print(botcode)






start()