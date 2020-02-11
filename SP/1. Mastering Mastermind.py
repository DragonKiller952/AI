import random
generated = []
solved = 0
tries = 0
for i in range(4):
    generated.append(random.choice('ABCDEF'))
print('Je kunt kiezen uit A, B, C, D, E en F')

while not solved:
    zwart = 0
    wit = 0
    if tries < 12:
        tries += 1
        print('Poging {}'.format(tries))
        given = input('Geef je reeks: ').upper()
        while True:
            if len(given) != 4:
                given = input('Geef een reeks van 4: ').upper()
            else:
                break

        for i in range(4):
            if given[i] == generated[i]:
                zwart += 1
            elif given[i] in generated:
                wit += 1

        if zwart == 4:
            print('Gefeliciteerd, je hebt in {} pogingen gewonnen!'.format(tries))
            solved = 1
        else:
            print('zwart = {}, wit = {}'.format(zwart, wit))

    else:
        print('Helaas, de reeks was {}{}{}{}'.format(generated[1], generated[2], generated[2], generated[3]))
        break
