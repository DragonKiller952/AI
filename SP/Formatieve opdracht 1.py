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


#Opg4:

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
