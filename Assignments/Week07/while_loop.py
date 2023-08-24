# Create a while loop to check if a number is positive
num = float(input('Enter a number with a positive value: '))

while num <= 0:
    print('Sorry that is a negaitive number.')
    num = float(input('Enter a number with a positive value: '))

print(f'The number you selected is {num}')

# Create a boolean to determine if you can have a piece of candy
print()
candy_decision = 'No'

while candy_decision.capitalize() == 'No':
    candy_decision = input('May I have a piece of candy (Yes/No)? ')

print()
print('Thank you!')
print()
