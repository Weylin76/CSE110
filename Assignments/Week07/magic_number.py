import random

num_of_guess = 1
rand_num = random.randint(1, 100)
player_guess = int(input('Pick a number from 1 to 100: '))

while rand_num != player_guess:
    if player_guess > rand_num:
        print('Your guess is too high!')
        player_guess = int(
            input('Try to guess again but a lower number this time: '))
    else:
        print('Your guess is too low!')
        player_guess = int(
            input('Try to guess again but a higher number this time: '))

    num_of_guess += 1

# display winning message to user
print(f'You guess correctly!  It only took you {num_of_guess} guesses.')
