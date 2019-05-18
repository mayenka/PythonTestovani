import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']    #to stejné jako podmínka s if


def random_play():
    '''z možností rock, scissors a paper vybere se stejnou pravděpodobností jednu variantu
    a tu vrátí'''
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock' and computer == 'scissors':
        return 'human'
    elif human == 'rock' and computer == 'paper':
        return 'computer'
    elif human == 'scissors' and computer == 'rock':
        return 'computer'
    elif human == 'scissors' and computer == 'paper':
        return 'human'
    elif human == 'paper' and computer == 'rock':
        return 'human'
    elif human == 'paper' and computer == 'scissors':
        return 'computer'


def main(load=input):
    # human = input('rock, paper or scissors? ')
    human = None    #None není validní, takže vím, že pak proběhne následný cyklus
    while not is_valid_play(human):
    # while human not in ['rock', 'paper', 'scissors']:
        human = load('rock, paper or scissors? ')

    # computer = random.choice(['rock', 'paper', 'scissors'])
    computer = random_play()

    print(computer)

    result = determine_game_result(human, computer)

    print(result)

if __name__ == '__main__':      #proměnná == řetezec
    main()

#     if human == computer:
#         print('it\'s a tie!')
#     elif human == 'rock' and computer == 'scissors':
#         print('you win!')
#     elif human == 'rock' and computer == 'paper':
#         print('you loose!')
#     elif human == 'scissors' and computer == 'rock':
#         print('you loose!')
#     elif human == 'scissors' and computer == 'paper':
#         print('you win!')
#     elif human == 'paper' and computer == 'rock':
#         print('you wins!')
#     elif human == 'paper' and computer == 'scissors':
#         print('you loose!')
# else:
#     print('mistake, please play again!')
