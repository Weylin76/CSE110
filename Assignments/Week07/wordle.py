import random
from five_letter_words import word_list


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

guess_list1 = []
guess_list2 = []
guess_list3 = []
guess_list4 = []
guess_list5 = []
guess_list6 = []

guess_lists = [guess_list1, guess_list2, guess_list3,
               guess_list4, guess_list5, guess_list6]

print(f'Hint: the word is {chosen_word}')

attempts = 6
correct_guess = False

for attempt in range(attempts):
    guess = input("Guess a word: ")
    while len(guess) != 5:
        print('You must guess 5 letter words only!')
        guess = input("Guess a word: ")

    guess_list = []

    for i in range(word_length):
        if chosen_word[i] == guess[i].lower():
            # Set the color to green
            guess_list.append(Color.GREEN + guess[i].upper() + Color.RESET)
        elif guess[i] in chosen_word:
            # Set the color yellow
            guess_list.append(Color.YELLOW + guess[i].lower() + Color.RESET)
        else:
            guess_list.append('_')

    guess_lists[attempt] = guess_list

    for prev_guess in guess_lists[:attempt + 1]:
        print(" ".join(prev_guess))

    if guess.lower() == chosen_word:
        print("Congratulations! You guessed the word.")
        correct_guess = True
        break
    elif attempt == 5:
        break
    else:
        print("Keep guessing!")

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
    elif attempt == 4:
        print()
        print('Results:')
        print(" ".join(guess_lists[0]))
        print(" ".join(guess_lists[1]))
        print(" ".join(guess_lists[2]))
        print(" ".join(guess_lists[3]))
        print(" ".join(guess_lists[4]))
        print(" ".join(guess_lists[5]))

if not correct_guess:
    print(f"Sorry, you're out of attempts. The word was '{chosen_word}'.")
