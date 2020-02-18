import random
import itertools

# bronnen
# https://stackoverflow.com/questions/47380999/how-to-make-a-list-with-all-possible-combinations


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


def computer_vs_user():
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


def computer_vs_computer():
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


if __name__ == "__main__":
    player = input('Is de computer de master? [Y/N]: ').upper()
    if player == 'Y':
        guesser = input('Is de computer de guesser? [Y/N]: ').upper()
        if guesser == 'Y':
            scores = []
            for i in range(100000):
                if i % 1000 == 0:
                    print('{}% done'.format((i / 100000) * 100))
                scores.append(computer_vs_computer())
            print(sum(scores) / len(scores))
            for i in range(1, 11):
                print('{}: {}%'.format(i, ((scores.count(i)) / len(scores)) * 100))
        elif guesser == 'N':
            computer_vs_user()
    elif player == 'N':
        guesser = input('Is de computer de guesser? [Y/N]: ').upper()
        if guesser == 'Y':
            user_vs_computer()
        elif guesser == 'N':
            print('Dit wordt niet ondersteunt')
