# gather user input
print()
while True:
    try:
        first_num = int(input('Enter a whole number for the first number: '))
        break  # Break the loop if a valid integer is entered
    except ValueError:
        print('Invalid input. Please enter a whole number.')

while True:
    try:
        second_num = int(input('Enter a whole number for the second number: '))
        break  # exit loop if data is valid
    except ValueError:
        print('Invalid input. Please enter a whole number.')

# Run comparsions calculations
print()
print('-'*40)
if first_num > second_num:
    print(f'{first_num} is larger than {second_num}')
elif first_num < second_num:
    print(f'{first_num} is less than {second_num}')
else:
    print(f'{first_num} and {second_num} are equal!')
print()
