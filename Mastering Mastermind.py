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
    gok = [1, 1, 2, 3]
    mogelijk = createans()
    hint = botstart(botcode, gok)
    if hint == [4, 0]:
        print('Gefelicteerd')
        start()
    else:
        mogelijk = eenfunctienaam(mogelijk, hint, gok)
        print(mogelijk)
        print(len(mogelijk))

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

def viergoed(mogelijk, gok, j):
    while j < len(mogelijk):
        e = []
        z = mogelijk[j]
        e.append(z.find(str(gok[0])))
        if e != -1:
            slicedz1 = z[4:]
            slicedz2 = z[:3]
            z = slicedz2 + '9' + slicedz1
        e.append(z.find(str(gok[1])))
        if e != -1:
            slicedz1 = z[4:]
            slicedz2 = z[:3]
            z = slicedz2 + '9' + slicedz1
        e.append(z.find(str(gok[2])))
        if e != -1:
            slicedz1 = z[4:]
            slicedz2 = z[:3]
            z = slicedz2 + '9' + slicedz1
        e.append(z.find(str(gok[3])))
        if e != -1:
            slicedz1 = z[4:]
            slicedz2 = z[:3]
            z = slicedz2 + '9' + slicedz1
        e.sort()
        print(e)
        if e[0] == -1:
            print("deze e verwijdert ie")
            mogelijk.pop(j)
            j -= 1
        else:
            j += 1
    if '6' not in gok:
        for woord in mogelijk:
            if '6' in woord:
                mogelijk.remove(woord)
    if '5' not in gok:
        for woord in mogelijk:
            if '5' in woord:
                mogelijk.remove(woord)
    if '4' not in gok:
        for woord in mogelijk:
            if '4' in woord:
                mogelijk.remove(woord)
    if '3' not in gok:
        for woord in mogelijk:
            if '3' in woord:
                mogelijk.remove(woord)
    if '2' not in gok:
        for woord in mogelijk:
            if '2' in woord:
                mogelijk.remove(woord)
    if '1' not in gok:
        for woord in mogelijk:
            if '1' in woord:
                mogelijk.remove(woord)
    return mogelijk

def driegoed(mogelijk, gok, j):
    while j < len(mogelijk):
        e = []
        e.append(mogelijk[j].find(str(gok[0])))
        e.append(mogelijk[j].find(str(gok[1])))
        e.append(mogelijk[j].find(str(gok[2])))
        e.append(mogelijk[j].find(str(gok[3])))
        e.sort()
        if e[0] == -1 and e[1] == -1:
            mogelijk.pop(j)
            j -= 1
        j += 1
    return mogelijk

def tweegoed(mogelijk, gok, j):
    while j < len(mogelijk):
        e = []
        e.append(mogelijk[j].find(str(gok[0])))
        e.append(mogelijk[j].find(str(gok[1])))
        e.append(mogelijk[j].find(str(gok[2])))
        e.append(mogelijk[j].find(str(gok[3])))
        e.sort()
        if e[0] == -1 and e[1] == -1 and e[2] == -1:
            mogelijk.pop(j)
            j -= 1
        j += 1
    return mogelijk

def eengoed(mogelijk, gok, j):
    while j < len(mogelijk):
        e = []
        e.append(mogelijk[j].find(str(gok[0])))
        e.append(mogelijk[j].find(str(gok[1])))
        e.append(mogelijk[j].find(str(gok[2])))
        e.append(mogelijk[j].find(str(gok[3])))
        e.sort()
        if sum(e) == -4:
            mogelijk.pop(j)
            j -= 1
        j += 1
    return mogelijk

def nulgoed(mogelijk, gok, j, nieuw):
    while j < len(mogelijk):
        e = []
        e.append(mogelijk[j].find(str(gok[0])))
        e.append(mogelijk[j].find(str(gok[1])))
        e.append(mogelijk[j].find(str(gok[2])))
        e.append(mogelijk[j].find(str(gok[3])))
        e.sort()
        if sum(e) == -4:
            nieuw.append(j)
        j += 1
    return nieuw


def eenfunctienaam(mogelijk, hint, gok):
    gokstring = ''.join(map(str, gok))
    mogelijk.remove(gokstring)
    if sum(hint) == 4:
        j = 0
        nieuw = viergoed(mogelijk, gok, j)
    else:
        if sum(hint) == 3:
            j = 0
            nieuw = driegoed(mogelijk, gok, j)
        else:
            if sum(hint) == 2:
                j = 0
                nieuw = tweegoed(mogelijk, gok, j)
            else:
                if sum(hint) == 1:
                    j = 0
                    nieuw = eengoed(mogelijk, gok, j)
                else:
                    if sum(hint) == 0:
                        j = 0
                        nieuw = []
                        nieuw = nulgoed(mogelijk, gok, j, nieuw)
    print(hint)
    if hint != [0,0]:
        j = 0
        nieuw = verbeterdefeedback(nieuw, gok, j, hint)
        print(len(nieuw))
        j = 0
        nieuw = wittepins(nieuw, gok, j, hint)
    return nieuw

def wittepins(nieuw, gok, j, hint):
    while j != len(nieuw):
        print('yeeeeeeeey')
        woord = nieuw[j]
        teller = 0
        if str(gok[0]) in woord and str(gok[0]) != woord[0]:
            teller += 1
        if str(gok[1]) in woord and str(gok[1]) != woord[1]:
            teller += 1
        if str(gok[2]) in woord and str(gok[2]) != woord[2]:
            teller += 1
        if str(gok[3]) in woord and str(gok[3]) != woord[3]:
            teller += 1
        print('TELLEEEEEEEEEEEER ' + str(teller))
        if teller == 4:
            j += 1
        else:
            nieuw.remove(woord)
            verbeterdefeedback(nieuw, gok, j, hint)
    return nieuw

def verbeterdefeedback(nieuw, gok, j, hint):
    while j != len(nieuw):
        woord = nieuw[j]
        teller = 0
        if str(gok[0]) == woord[0]:
            teller += 1
        if str(gok[1]) == woord[1]:
            teller += 1
        if str(gok[2]) == woord[2]:
            teller += 1
        if str(gok[3]) == woord[3]:
            teller += 1
        if teller == hint[0]:
            j += 1
        else:
            nieuw.remove(woord)
            verbeterdefeedback(nieuw, gok, j, hint)
    return nieuw

def botstart(code, gok):
    poging = 0
    nieuw = [0, 0, 0, 0]
    hint = [0, 0]
    lengtehint = 0
    aanpascode = [0, 0, 0, 0]
    while lengtehint != 4:
        if code[lengtehint] == gok[lengtehint]:
            nieuw[lengtehint] = 1
            aanpascode[lengtehint] = 99
            hint[0] = hint[0] + 1
        lengtehint += 1
    lengtehint = 0
    while lengtehint != 4:
        print(lengtehint)
        if gok[lengtehint] in code:
            if aanpascode[lengtehint] != 99:
                aanpas = int(aanpascode.index(nieuw[lengtehint]))
                aanpascode[aanpas] = 'gebruikt'
                hint[1] = hint[1] + 1
#               else:
#                   aanpas = int(aanpascode.index(nieuw[lengtehint]))
#                   aanpascode[aanpas] = 'gebruikt'
#                   hint[1] = hint[1] + 1
        lengtehint += 1
    poging += 1
    return hint

start()