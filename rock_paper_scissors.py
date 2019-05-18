import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']    #to stejné jako podmínka s if









human = input('rock, paper or scissors? ')

while human not in ['rock', 'paper', 'scissors']:
    human = input('rock, paper or scissors? ')

computer = random.choice(['rock', 'paper', 'scissors'])

print(computer)

if human == computer:
    print('it\'s a tie!')
elif human == 'rock' and computer == 'scissors':
    print('you win!')
elif human == 'rock' and computer == 'paper':
    print('you loose!')
elif human == 'scissors' and computer == 'rock':
    print('you loose!')
elif human == 'scissors' and computer == 'paper':
    print('you win!')
elif human == 'paper' and computer == 'rock':
    print('you wins!')
elif human == 'paper' and computer == 'scissors':
    print('you loose!')
else:
    print('mistake, please play again!')
