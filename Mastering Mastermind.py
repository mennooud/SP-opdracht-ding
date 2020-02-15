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
    gok = [1, 1, 2, 2]
    mogelijk = createans()
    hint = botstart(botcode, gok)
    mogelijk = eenfunctienaam(mogelijk, hint, gok)
    print(mogelijk)

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

def driegoed(mogelijk, gok, j):
    try:
        while j < len(mogelijk):
            e = []
            e.append(mogelijk[j].find(str(gok[0])))
            e.append(mogelijk[j].find(str(gok[1])))
            e.append(mogelijk[j].find(str(gok[2])))
            e.append(mogelijk[j].find(str(gok[3])))
            e.sort()
            if e[0] == -1 and e[1] == -1:
                mogelijk.pop(j)
                driegoed(mogelijk, gok, j)
            j += 1
    except RecursionError:
        print(mogelijk)
    except IndexError:
        print(mogelijk)
    return mogelijk

def tweegoed(mogelijk, gok, j):
    try:
        while j < len(mogelijk):
            e = []
            e.append(mogelijk[j].find(str(gok[0])))
            e.append(mogelijk[j].find(str(gok[1])))
            e.append(mogelijk[j].find(str(gok[2])))
            e.append(mogelijk[j].find(str(gok[3])))
            e.sort()
            if e[0] == -1 and e[1] == -1 and e[2] == -1:
                mogelijk.pop(j)
                driegoed(mogelijk, gok, j)
            j += 1
    except RecursionError:
        print(mogelijk)
    except IndexError:
        print(mogelijk)
    return mogelijk

def eengoed(mogelijk, gok, j):
    try:
        while j < len(mogelijk):
            e = []
            e.append(mogelijk[j].find(str(gok[0])))
            e.append(mogelijk[j].find(str(gok[1])))
            e.append(mogelijk[j].find(str(gok[2])))
            e.append(mogelijk[j].find(str(gok[3])))
            e.sort()
            if sum(e) == -4:
                mogelijk.pop(j)
                driegoed(mogelijk, gok, j)
            j += 1
    except RecursionError:
        return mogelijk
    except IndexError:
        return mogelijk
    return mogelijk



def eenfunctienaam(mogelijk, hint, gok):
    if sum(hint) == 3:
        j = 0
        return driegoed(mogelijk, gok, j)
    else:
        if sum(hint) == 2:
            j = 0
            return tweegoed(mogelijk, gok, j)
        else:
            if sum(hint) == 1:
                j = 0
                return eengoed(mogelijk, gok, j)

    #j = 0
    #print(len(mogelijk))
    #while j != len(mogelijk):
    #    a = mogelijk[j].find('1')
    #    if a != -1:
    #        mogelijk.pop(j)
    #        eenfunctienaam(mogelijk)
    #    j += 1
    #return mogelijk

def botstart(code, gok):
    poging = 0
    nieuw = [0, 0, 0, 0]
    hint = [0, 0]
    lengtehint = 0
    aanpascode = [0, 0, 0, 0]
    if nieuw == code:
        print("Gefeliciteerd")
    else:
        while lengtehint != 3:
            if code[lengtehint] == gok[lengtehint]:
                nieuw[lengtehint] = 1
                aanpascode[lengtehint] = 99
                hint[0] = hint[0] + 1
            lengtehint += 1
        lengtehint = 0
        while lengtehint != 3:
            if gok[lengtehint] in code:
                if aanpascode[lengtehint] == 99:
                    continue
                else:
                    aanpas = int(aanpascode.index(nieuw[lengtehint]))
                    aanpascode[aanpas] = 'gebruikt'
                    hint[1] = hint[1] + 1
            lengtehint += 1
        poging += 1
        return hint



menscode()

start()