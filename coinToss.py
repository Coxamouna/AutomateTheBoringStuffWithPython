import random

coin = ['heads', 'tails']

guess = ''
while guess not in coin:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = coin[random.randint(0, 1)] # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')