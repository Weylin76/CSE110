import random
from five_letter_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# store guesses
guess_list1 = []
guess_list2 = []
guess_list3 = []
guess_list4 = []
guess_list5 = []

print(f'Hint: the word is {chosen_word}')

guess1 = input('Guess a word:')
for i in range(word_length):
    if chosen_word[i] == guess1[i]:
        guess_list1.append(guess1[i].upper())
    elif guess1[i] in chosen_word:
        guess_list1.append(guess1[i].lower())
    else:
        guess_list1.append('_')
print(f"{' '.join(guess_list1)}")

guess2 = input('Guess a word:')
for i in range(word_length):
    if chosen_word[i] == guess2[i]:
        guess_list2.append(guess2[i].upper())
    elif guess_list2[i] in chosen_word:
        guess_list2.append(guess2[i].lower())
    else:
        guess_list2.append('_')
print(f"{' '.join(guess_list2)}")
