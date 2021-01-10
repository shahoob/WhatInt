from random import randint
import click

@click.command()
@click.option('-m', '--max', default=10, help='The max range for generating the integer (that you\'re trying to guess)')
@click.option('-M', '--min', default=0, help='The min range for generating the integer (that you\'re trying to guess)')
def game(min, max):
    answer: int = randint(min, max)
    done: bool = False
    tries: int = 0
    triedInts: list[int] = []

    while not done:
        chosenIn: str = input('what integer: ')
        if chosenIn == 'stop': break
        chosenInt: int = int(chosenIn)
        tries += 1
        triedInts.append(chosenInt)
        if chosenInt < answer:
            print('far behind.')
        elif chosenInt > answer:
            print('too far away')
        elif chosenInt == answer:
            print('yes')
            done = True

    if not done:
        print('you have canceled the game')
        return

    print(f'you toke {tries} tries to get {answer}.')
    if tries == 1:
        print('how did you make a single try to get it right')
        print('impossible')

    print('you have used these integers:')
    [print(x) for x in triedInts]

if __name__ == '__main__':
    game()
