import random

#Ik weet niet hoe ik verder kom met hetgeen wat ik al heb, als in ik weet niet hoe ik de beste keuze voor de pc nu moet laten uitrekenen. Ook weet ik niet hoe ik met de zwarte pins precies moet werken.
#Heeft u hier een tip voor of iets waardoor ik weer verder kan?


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
    mogelijk = createans()
    code = ''.join(map(str, botcode))
    eenfunctienaam(mogelijk, code)

def createans():
    possibleans = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            possibleans.append(answer)
    print(possibleans)
    return possibleans

def eenfunctienaam(mogelijk, code):
    lives = 10
    attempts = 0

    while lives > 0:
        print(mogelijk)
        gok = mogelijk[0]
        print(gok)
        feedback = botstart(code, gok)

        for i in reversed(mogelijk):
            item_feedback = botstart(gok, i)

            if feedback != item_feedback:
                mogelijk.remove(i)

        lives -= 1
        attempts += 1

        if code == gok:
            print('gevonden')
            print(attempts)
            break
        else:
            if lives == 0:
                print('game over')
    start()

def botstart(strcode, gok):
    code = []
    for item in strcode:
        code.append(int(item))
    nieuw = [0, 0, 0, 0]
    hint = [0, 0]
    lengtehint = 0
    aanpascode = [0, 0, 0, 0]
    while lengtehint != 4:
        if code[lengtehint] == int(gok[lengtehint]):
            print(code[lengtehint])
            print(gok[lengtehint])
            nieuw[lengtehint] = 1
            aanpascode[lengtehint] = 99
            hint[0] = hint[0] + 1
        else:
            aanpascode[lengtehint] = code[lengtehint]
        lengtehint += 1
    lengtehint = 0
    while lengtehint != 4:
        if int(gok[lengtehint]) in aanpascode:
            if nieuw[lengtehint] != 1:
                hint[1] += 1
                aanpascode[int(gok[lengtehint])-1] = 9
        lengtehint += 1
    print(hint)
    return hint

#code = []
#code.append(input('getal'))
#code.append(input('getal'))
#code.append(input('getal'))
#code.append(input('getal'))
#strcode = '1134'
#botstart(strcode, code)

start()