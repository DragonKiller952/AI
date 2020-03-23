# Opg1:

lengte = int(input('hoe groot? '))
lenwhile = 1

for i in range(1, lengte+1):
    print('*' * i)

for j in reversed(range(1, lengte)):
    print('*' * j)

while lenwhile <= lengte:
    print('*' * lenwhile)
    lenwhile += 1

lenwhile -= 2

while lenwhile > 0:
    print('*' * lenwhile)
    lenwhile -= 1

# Opg2:

zin1 = input('Geef een string: ')
zin2 = input('Geef een string: ')

if zin1 == zin2:
    print('De strings zijn hetzelfde')
else:
    if len(zin1) != len(zin2):
        if len(zin1) > len(zin2):
            controlezin = zin1
            fixzin = zin2 + ('*' * (len(zin1) - len(zin2)))
        else:
            controlezin = zin2
            fixzin = zin1 + ('*' * (len(zin2) - len(zin1)))

        for i in range(len(controlezin)):
            if controlezin[i] != fixzin[i]:
                verschil = i
                break
        print('Het eerste verschil zit op index: {}'.format(verschil))
    else:
        for i in range(len(zin1)):
            if zin1[i] != zin2[i]:
                verschil = i
                break
        print('Het eerste verschil zit op index: {}'.format(verschil))

# Opg3a:


def count(lst, target):
    amount = 0
    for i in range(len(lst)):
        if lst[i] == target:
            amount += 1
    return amount

# Opg3b:


def biggestdiff(lst):
    biggestdiff = 0
    for i in range(len(lst)):
        if i+1 != len(lst):
            diff = abs(lst[i] - lst[i+1])
            if diff > biggestdiff:
                biggestdiff = diff
    return biggestdiff

# Opg3c


def check(lst):
    if count(lst, 0) < 12:
        if count(lst, 0) < count(lst, 1):
            return'Deze lijst voldoet'
        else:
            return'Deze lijst voldoet niet'
    else:
        return'Deze lijst voldoet niet'


# Opg4:

zin = (input('Geef een zin: ')).upper()
zintest1 = list(zin)
palintest1 = list(reversed(zin))

if zintest1 == palintest1:
    print('Dit is een palindroom')
else:
    print('Dit is geen palindroom')

zintest2 = list(zin)
palintest2 = []

for i in reversed(range(len(zintest2))):
    palintest2.append(zintest2[i])

if zintest2 == palintest2:
    print('Dit is een palindroom')
else:
    print('Dit is geen palindroom')

# Opg5:


def sort(lst):
    sort = 1
    while sort:
        sort = 0
        for i in range(len(lst)):
            if not i + 1 > len(lst) - 1:
                if lst[i + 1] < lst[i]:
                    sort = 1
                    x = lst[i]
                    y = lst[i + 1]
                    lst[i] = y
                    lst[i + 1] = x
    return lst


# Opg6:

def gemiddelde(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    average = total / len(lst)
    return average


def gemiddeldegemiddelde(lstlst):
    gemiddeldelst = []
    for i in range(len(lstlst)):
        gemiddeldelst.append(gemiddelde(lstlst[i]))
    result = gemiddelde(gemiddeldelst)
    return result


# Opg7:

import random

choice = int(input('Kies een nummer van 0-10: '))
number = random.randint(0, 10)

while choice != number:
    choice = int(input('Dat is niet het juiste nummer, probeer opnieuw: '))
    number = random.randint(0, 10)

print('Dat was het juiste nummer!')

# Opg8:

invoer = 'InvoerFormatieveOpdracht1Opg8'
uitvoer = 'UitvoerFormatieveOpdracht1Opg8'
inv = open(invoer, 'r')
uit = open(uitvoer, 'w')
text = []

inhoud = inv.readlines()
for i in range(len(inhoud)):
    lettertest = 0
    current2 = []
    for j in range(len(inhoud[i])):
        if inhoud[i] != '\n':
            current = inhoud[i][j]
            if lettertest:
                current2.append(current)
            else:
                if current != ' ':
                    current2.append(current)
                    lettertest = 1
    mergecurrent = ''.join(current2)
    if mergecurrent:
        text.append(mergecurrent)
for i in range(len(text)):
    uit.write(text[i])

# Opg9:


def move(ch, n):
    lst = list(str(ch))
    newlst = [0, 0, 0, 0, 0, 0, 0, 0]
    if n > 0:
        movement = n % 8
        for i in range(8):
            newlst[i - 8 + movement] = lst[i]
        result = ''.join(newlst)
        return result
    elif n < 0:
        movement = n % -8
        for i in range(8):
            newlst[i + movement] = lst[i]
        result = ''.join(newlst)
        return result
    else:
        return ch


# Opg10:

def fibonaci(n):
    result = [0, 1]
    current = [0, 0]
    if n == 0:
        return 0
    else:
        for i in range(n-1):
            current[0] = result[0]
            current[1] = result[1]
            result[0] = current[1]
            result[1] = current[0] + current[1]
        return result[1]


# Opg11:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
cipher = []
number = 0
tekst = list(input('Geef een tekst: '))
rotatie = int(input('Geef een rotatie: '))
if rotatie >= 0:
    actrotatie = rotatie % 26
    for i in range(len(tekst)):
        if (tekst[i].isupper()):
            current = tekst[i].lower()
            if current not in alphabet:
                cipher.append(tekst[i])
            else:
                for j in range(len(alphabet)):
                    if alphabet[j] == current:
                        number = j
                        break
                cipher.append(alphabet[-26 + number + rotatie].upper())

        else:
            if tekst[i] not in alphabet:
                cipher.append(tekst[i])
            else:
                for j in range(len(alphabet)):
                    if alphabet[j] == tekst[i]:
                        number = j
                        break
                cipher.append(alphabet[-26 + number + rotatie])
else:
    actrotatie = rotatie % -26
    for i in range(len(tekst)):
        if (tekst[i].isupper()):
            current = tekst[i].lower()
            if current not in alphabet:
                cipher.append(tekst[i])
            else:
                for j in range(len(alphabet)):
                    if alphabet[j] == current:
                        number = j
                        break
                cipher.append(alphabet[number + rotatie].upper())

        else:
            if tekst[i] not in alphabet:
                cipher.append(tekst[i])
            else:
                for j in range(len(alphabet)):
                    if alphabet[j] == tekst[i]:
                        number = j
                        break
                cipher.append(alphabet[number + rotatie])


print(''.join(cipher))

# Opg12:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
