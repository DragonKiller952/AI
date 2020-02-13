# bronnen
# https://stackoverflow.com/questions/47380999/how-to-make-a-list-with-all-possible-combinations


def UserVsComputer():
    import random
    generated = []
    lengtereeks = 4
    tries = 0
    for i in range(lengtereeks):
        generated.append(random.choice('ABCDEF'))
    print('Je kunt kiezen uit A, B, C, D, E en F')


    def feedback(secret, guess):
        feedbacksecret = list(secret)
        feedbackguess = list(guess)
        zwart = 0
        wit = 0
        move1 = 0
        move2 = 0

        for x in range(4):
            if feedbacksecret[x + move1] == feedbackguess[x + move1]:
                del feedbackguess[x + move1]
                del feedbacksecret[x + move1]
                zwart += 1
                move1 -= 1
        if len(feedbackguess) > 0:
            for x in range(len(feedbackguess)):
                if feedbackguess[x + move2] in feedbacksecret:
                    feedbacksecret.remove(feedbackguess[x + move2])
                    del feedbackguess[x + move2]
                    wit += 1
                    move2 -= 1
        return zwart, wit


    while True:
        if tries < 10:
            tries += 1
            print('Poging {}'.format(tries))
            given = list(input('Geef je reeks: ').upper())
            while True:
                if len(given) != lengtereeks:
                    given = list(input('Geef een reeks van {}: '.format(lengtereeks)).upper())
                else:
                    break

            result = feedback(generated, given)
            if result[0] == 4:
                print('Gefeliciteerd, je hebt gewonnen!')
                break
            else:
                print('zwart = {}, wit = {}'.format(result[0], result[1]))

        else:
            print('Helaas, de reeks was {}{}{}{}'.format(generated[1], generated[2], generated[2], generated[3]))
            break


def ComputerVsUser():
    import itertools

    def comb(lst, length):
        return sorted(list(itertools.product(lst, repeat=length)))

    possibilities = comb('ABCDEF', 4)
    mastercode = input('Geef de mastercode:').upper()
    tries = 0

    def feedback(secret, guess):
        feedbacksecret = list(secret)
        feedbackguess = list(guess)
        zwart = 0
        wit = 0
        move1 = 0
        move2 = 0

        for x in range(4):
            if feedbacksecret[x + move1] == feedbackguess[x + move1]:
                del feedbackguess[x + move1]
                del feedbacksecret[x + move1]
                zwart += 1
                move1 -= 1
        if len(feedbackguess) > 0:
            for x in range(len(feedbackguess)):
                if feedbackguess[x + move2] in feedbacksecret:
                    feedbacksecret.remove(feedbackguess[x + move2])
                    del feedbackguess[x + move2]
                    wit += 1
                    move2 -= 1
        return zwart, wit

    def checkpossibilities(lst, guess, given):
        checklst = list(lst)
        move = 0
        for i in range(len(lst)):
            check = feedback(checklst[i+move], guess)
            if check != given:
                del checklst[i+move]
                move -= 1

        return checklst

    while True:
        if tries < 10:
            tries += 1
            print('poging {}'.format(tries))
            print(possibilities[0])
            givenzwart= int(input('Geef hoeveel zwarte pinnen: '))
            givenwit = int(input('Geef hoeveel witte pinnen: '))
            given = (givenzwart, givenwit)
            if given == (4, 0):
                print('De computer heeft gewonnen in {} pogingen!'.format(tries))
                break
            else:
                possibilities = checkpossibilities(possibilities, possibilities[0], given)
        else:
            print('De computer heeft verloren')
            break


player = input('Is de computer de master? [Y/N]: ').upper()
if player == 'Y':
    guesser = input('Is de computer de guesser? [Y/N]: ').upper()
    if guesser == 'Y':
        print('Dit wordt niet ondersteunt')
    elif guesser == 'N':
        ComputerVsUser()
elif player == 'N':
    guesser = input('Is de computer de guesser? [Y/N]: ').upper()
    if guesser == 'Y':
        UserVsComputer()
    elif guesser == 'N':
        print('Dit wordt niet ondersteunt')
