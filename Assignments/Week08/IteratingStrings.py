# # CORE REQUIREMENTS 01 - 02
# word = 'Commitment'

# for char in word:
#     print(char)

# fav_letter = input('What is your favorite letter:')
# for char in word:
#     if fav_letter == char:
#         print(char.upper(), end="")
#     else:
#         print(char.lower(), end="")

# # CORE REQUIREMENTS 03
# print()
# for char in word:
#     if fav_letter == char:
#         print('_', end="")
#     else:
#         print(char.lower(), end="")


# # STRETCH CHALLENGE
# print()
# first_name = "Brigham"
# # Notice by using enumerate, we specify both i and letter
# for i, letter in enumerate(first_name):
#     print(f"The letter {letter} is at position {i}")

# STRETCH CHALLENGE 1
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
new_quote = []

index = int(input("Enter a position index: "))

for i, letter in enumerate(quote):
    # print(f'Index: {i}, letter: {letter}.', end='')
    if i % index == 0:
        letter = quote[i].upper()
    new_quote.append(letter)
    new_str = "".join(new_quote)

print(new_str)
