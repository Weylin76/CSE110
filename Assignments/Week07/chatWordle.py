import random
from five_letter_words import word_list

# create a color library


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# store guesses
guess_list1 = []
guess_list2 = []
guess_list3 = []
guess_list4 = []
guess_list5 = []
guess_list6 = []

# store guesses
guess_lists = [guess_list1, guess_list2, guess_list3,
               guess_list4, guess_list5, guess_list6]

print(f'Hint: the word is {chosen_word}')

# limit player to 5 rounds of playing
attempts = 6

# outer loop to track user attempts
for attempt in range(attempts):
    print()
    while True:
        guess = input("Guess a word: ")
        if len(guess) == word_length:
            break
        else:
            print("Your guess should be exactly 5 characters long.")

    guess_list = []

    # Check if user guess contian letter in the chosen word
    for i in range(word_length):
        if chosen_word[i] == guess[i].lower():
            # guess_list.append(guess[i].upper())
            # Set the color to green
            guess_list.append(Color.GREEN + guess[i].upper() + Color.RESET)
        elif guess[i].lower() in chosen_word:
            # set to yellow
            guess_list.append(Color.YELLOW + guess[i].lower() + Color.RESET)
        else:
            guess_list.append('_')

    # prints user guess in a string format
    guess_lists[attempt] = guess_list
    print(" ".join(guess_list))

    # condition to check if play wins
    if chosen_word.lower() == guess:
        print('You win!')
        break

    # allows the player to see all previous attempts
    if attempt == 1:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
    elif attempt == 2:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
        print(" ".join(guess_lists[2]))
    elif attempt == 3:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
        print(" ".join(guess_lists[2]))
        print(" ".join(guess_lists[3]))
    elif attempt == 4:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
        print(" ".join(guess_lists[2]))
        print(" ".join(guess_lists[3]))
        print(" ".join(guess_lists[4]))
    elif attempt == 5:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
        print(" ".join(guess_lists[2]))
        print(" ".join(guess_lists[3]))
        print(" ".join(guess_lists[4]))
        print(" ".join(guess_lists[5]))

# if player loses the chosen word is displayed
if chosen_word.upper() != guess:
    print(f'The word was {chosen_word.upper()}.')
