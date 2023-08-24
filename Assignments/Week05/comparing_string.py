# gather input from the user
print()
while True:
    try:
        user_fav_animal = input('What is your favorite animal? ')
        if user_fav_animal.isalpha():
            break  # Exit the loop because only letters were entered
        else:
            raise ValueError  # Raise a ValueError if non-alphabetic characters are present
    except ValueError:
        print('Invalid input. Please enter alphabetic characters only.')

my_fav_aminal = 'tiger'

# Perform the string comparisons
if user_fav_animal.lower() != my_fav_aminal:
    print(f'{user_fav_animal.capitalize()} is a great animal!')
else:
    print(f'{user_fav_animal.capitalize()} is my favorite animal too!')
print()
