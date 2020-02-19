import random
import itertools

# bronnen
# https://stackoverflow.com/questions/47380999/how-to-make-a-list-with-all-possible-combinations
# https://en.wikipedia.org/wiki/Mastermind_(board_game)#Five-guess_algorithm
# YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi
# Lucas van der Horst


def comb(lst, length):
    return sorted(list(itertools.product(lst, repeat=length)))


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


def nextguess1(possibilities, allposs):
    allfeedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                   (3, 0), (4, 0)]
    maximalen = []
    for i in range(len(possibilities)):
        biggest = 0
        for j in range(len(allfeedback)):
            currentcheck = checkpossibilities(allposs, possibilities[i], allfeedback[j])
            if len(currentcheck) > biggest:
                biggest = len(currentcheck)
        maximalen.append(biggest)
    minmaxnumber = min(maximalen)
    for i in range(len(maximalen)):
        if maximalen[i] == minmaxnumber:
            minmaxlocatie = i
            break

    return possibilities[minmaxlocatie]


def nextguess2(possibilities, allposs):
    allfeedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                   (3, 0), (4, 0)]
    minimalen = []
    for i in range(len(possibilities)):
        biggest = 1296
        for j in range(len(allfeedback)):
            currentcheck = checkpossibilities(allposs, possibilities[i], allfeedback[j])
            if biggest > len(currentcheck) > 0:
                biggest = len(currentcheck)
        minimalen.append(biggest)
    maxminnumber = max(minimalen)
    for i in range(len(minimalen)):
        if minimalen[i] == maxminnumber:
            maxminlocatie = i
            break

    return possibilities[maxminlocatie]


def checkpossibilities(lst, guess, given):
    checklst = list(lst)
    move = 0
    for i in range(len(lst)):
        check = feedback(checklst[i+move], guess)
        if check != given:
            del checklst[i+move]
            move -= 1

    return checklst


def user_vs_computer():
    generated = []
    lengtereeks = 4
    tries = 0
    for i in range(lengtereeks):
        generated.append(random.choice('ABCDEF'))
    print('Je kunt kiezen uit A, B, C, D, E en F')

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


def computer_vs_user1():  # Deze code voert "A Simple Strategy" uit
    possibilities = comb('ABCDEF', 4)

    tries = 0
    while True:
        if tries < 10:
            tries += 1
            print('poging {}'.format(tries))
            print(possibilities[0])
            givenzwart = int(input('Geef hoeveel zwarte pinnen: '))
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


def computer_vs_user2():  # Deze code voert "A Worst Case Strategy" uit met behulp van de info uit de bron
    possibilities = comb('ABCDEF', 4)
    allposs = comb('ABCDEF', 4)

    tries = 0
    while True:
        if tries < 10:
            tries += 1
            print('Volgende stap berekenen...')
            chosenguess = nextguess1(possibilities, allposs)
            print('poging {}'.format(tries))
            print('nog {} mogelijkheden'.format(len(possibilities)))
            print(chosenguess)
            givenzwart = int(input('Geef hoeveel zwarte pinnen: '))
            givenwit = int(input('Geef hoeveel witte pinnen: '))
            given = (givenzwart, givenwit)
            if given == (4, 0):
                print('De computer heeft gewonnen in {} pogingen!'.format(tries))
                break
            else:
                possibilities = checkpossibilities(possibilities, chosenguess, given)
        else:
            print('De computer heeft verloren')
            break


def computer_vs_user3():  # Deze code doet het zelfde als computer_vs_user2, alleen kiest hij
    # inplaats van minmax, de maxmin
    possibilities = comb('ABCDEF', 4)
    allposs = comb('ABCDEF', 4)

    tries = 0
    while True:
        if tries < 10:
            tries += 1
            print('Volgende stap berekenen...')
            chosenguess = nextguess2(possibilities, allposs)
            print('poging {}'.format(tries))
            print('nog {} mogelijkheden'.format(len(possibilities)))
            print(chosenguess)
            givenzwart = int(input('Geef hoeveel zwarte pinnen: '))
            givenwit = int(input('Geef hoeveel witte pinnen: '))
            given = (givenzwart, givenwit)
            if given == (4, 0):
                print('De computer heeft gewonnen in {} pogingen!'.format(tries))
                break
            else:
                possibilities = checkpossibilities(possibilities, chosenguess, given)
        else:
            print('De computer heeft verloren')
            break


# De volgende functies zijn voor automatisch testen


def computer_vs_computer1():
    generated = []
    lengtereeks = 4
    tries = 0
    for i in range(lengtereeks):
        generated.append(random.choice('ABCDEF'))

    possibilities = comb('ABCDEF', 4)

    while True:
        if tries < 10:
            tries += 1
            # print('poging {}'.format(tries))
            # print(possibilities[0])
            result = feedback(generated, possibilities[0])
            if result == (4, 0):
                # print('De computer heeft gewonnen in {} pogingen!'.format(tries))
                return tries
            else:
                possibilities = checkpossibilities(possibilities, possibilities[0], result)
        else:
            # print('De computer heeft verloren')
            # print('Helaas, de reeks was {}{}{}{}'.format(generated[1], generated[2], generated[2], generated[3]))
            print(generated)
            return tries


def computer_vs_computer2():
    possibilities = comb('ABCDEF', 4)
    allposs = comb('ABCDEF', 4)

    generated = []
    lengtereeks = 4
    tries = 0
    for i in range(lengtereeks):
        generated.append(random.choice('ABCDEF'))

    while True:
        if tries < 10:
            tries += 1
            chosenguess = nextguess1(possibilities, allposs)
            result = feedback(generated, chosenguess)
            if result == (4, 0):
                return tries
            else:
                possibilities = checkpossibilities(possibilities, chosenguess, result)
        else:
            return tries


def computer_vs_computer3():
    possibilities = comb('ABCDEF', 4)
    allposs = comb('ABCDEF', 4)

    generated = []
    lengtereeks = 4
    tries = 0
    for i in range(lengtereeks):
        generated.append(random.choice('ABCDEF'))

    while True:
        if tries < 10:
            tries += 1
            chosenguess = nextguess2(possibilities, allposs)
            result = feedback(generated, chosenguess)
            if result == (4, 0):
                return tries
            else:
                possibilities = checkpossibilities(possibilities, chosenguess, result)
        else:
            return tries


if __name__ == "__main__":
    # Deze statements halen uit jouw antwoorden hoe je het spel wil spelen
    player = input('Is de computer de master? [Y/N]: ').upper()
    if player == 'Y':
        guesser = input('Is de computer de guesser? [Y/N]: ').upper()
        if guesser == 'Y':
            # Deze code kan gebruikt worden om de computer het algoritme 10 keer te laten testen, en hiervan de
            # resultaten weer te laten geven. dit kan best lang duren, dus het wordt aangeraden om het handmatig
            # te testen
            kind = input('Welke versie wil je testen? [1/2/3]: ')
            if kind == '1':
                scores = []
                print('Bezig met testen...')
                for i in range(10):
                    scores.append(computer_vs_computer1())
                print('gemiddelde: {}'.format(sum(scores) / len(scores)))
                for i in range(1, 11):
                    print('{}: {}%'.format(i, ((scores.count(i)) / len(scores)) * 100))
            elif kind == '2':
                scores = []
                print('Bezig met testen...')
                print('Dit duurt ongeveer 15 minuten')
                for i in range(10):
                    scores.append(computer_vs_computer2())
                print('gemiddelde: {}'.format(sum(scores) / len(scores)))
                for i in range(1, 11):
                    print('{}: {}%'.format(i, ((scores.count(i)) / len(scores)) * 100))
            elif kind == '3':
                scores = []
                print('Bezig met testen...')
                print('Dit duurt ongeveer 15 minuten')
                for i in range(10):
                    scores.append(computer_vs_computer3())
                print('gemiddelde: {}'.format(sum(scores) / len(scores)))
                for i in range(1, 11):
                    print('{}: {}%'.format(i, ((scores.count(i)) / len(scores)) * 100))
        elif guesser == 'N':
            # Met deze code kan je zelf tegen de computer spelen
            user_vs_computer()
    elif player == 'N':
        guesser = input('Is de computer de guesser? [Y/N]: ').upper()
        if guesser == 'Y':
            # Met deze code speelt de computer tegen jou
            kind = input('Welke versie wil je spelen? [1/2/3]: ')
            if kind == '1':
                computer_vs_user1()
            elif kind == '2':
                computer_vs_user2()
            elif kind == '3':
                computer_vs_user3()
        elif guesser == 'N':
            # hiermee zou je tegen een andere speler kunnen spelen
            print('Dit wordt niet ondersteunt')
