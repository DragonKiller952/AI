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


