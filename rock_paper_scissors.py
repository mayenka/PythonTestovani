import random

human = input('rock, paper or scissors? ')

while human not in ['rock', 'paper', 'scissors']:
    human = input('rock, paper or scissors? ')

computer = random.choice(['rock', 'paper', 'scissors'])

print(computer)

if human == computer:
    print('it\'s a tie!')
elif human == 'rock' and computer == 'scissors':
    print('human wins!')
elif human == 'rock' and computer == 'paper':
    print('computer wins!')
elif human == 'scissors' and computer == 'rock':
    print('computer wins!')
elif human == 'scissors' and computer == 'paper':
    print('human wins!')
elif human == 'paper' and computer == 'rock':
    print('human wins!')
elif human == 'paper' and computer == 'scissors':
    print('computer wins!')
else:
    print('mistake, please play again!')
