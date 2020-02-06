alfabet = 'abcdefghijklmnopqrstuvwxyz'
woord = input("Geef een woord")
key = int(input("Geef een key"))
nwoord = ""
for character in woord:
    positie = alfabet.find(character)
    npositie = positie + key
    while npositie > 26:
        npositie -= 26
    nwoord += alfabet[npositie]
print(nwoord)