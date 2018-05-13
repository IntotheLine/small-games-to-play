# This is a guess the number game.

import random
print('Hello Dandy and BatGirls, what is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well Dandy or BatGirl, ' + name + ', I think of a number between 1 and 20')

for guessesTaken in range(1, 7):
    print('Enter your guess.')
    guess = int(input())

    if guess < secretNumber:
        print('tool low, fail')
    elif guess > secretNumber:
        print('too high, superfail')
    else:
        break  # This condition is for the correct guess :)

if guess == secretNumber:
    print('GJ' + name + '! You took' + str(guessesTaken) + 'times!')
else:
    print('fail, the correct one' + str(secretNumber))

print('you took ' + str(guessesTaken) + ' guesses.')
