import random as random_number
import sys
def roll_dice_and_compute_sum(ndice):
    print ('rolldce')
    return sum([random_number.randint(1, 6) for i in range(ndice)])

def computer_guess(ndice):
    print ('comp')
    return random_number.randint(ndice, 6*ndice)

def player_guess(ndice):
    print ('pguess')
    return int(input('Guess the sum of the no of eyes in the next throw: '))

def play_one_round(ndice, capital, guess_function):
    print ('play1')
    guess = guess_function(ndice)
    throw = roll_dice_and_compute_sum(ndice)
    print(throw)
    if guess == throw:
        capital += guess
    else:
        capital -= 1
    return capital, throw, guess

winner = 0
def play(nrounds, ndice=2):
    print ('play')
    #start capital
    player_capital = computer_capital = nrounds # start capital

    for i in range(nrounds):
        player_capital, throw, guess = play_one_round(ndice, player_capital, player_guess)
        print ('YOU guessed %d, got %d' % (guess, throw))
        if player_capital == 0:
            print('Machine won!')
            computer_capital, throw, guess = play_one_round(ndice, computer_capital, computer_guess)
            print ('Machine guessed %d, got %d' % (guess, throw))
        if computer_capital == 0:
            print('You won!')
        print ('Status: you have %d euros, machine has %d euros\n' % (player_capital,computer_capital))

    if computer_capital > player_capital:
        winner = 'Machine'
        print(winner ,'won')
    else:
        winner = 'You'
        print (winner, 'won!')
play(2,4)