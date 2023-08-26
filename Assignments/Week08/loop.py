dogs = ['Cocoa', 'Cheaters']

# for dog in dogs:
#     print(dog)

# for i in range(10):
#     if i % 2 == 0:
#         print(i)

# name = ''

# while name != 'Cocoa':
#     print('Not the best dog!')
#     name = input('Who is the best dog? ')

# print('Correct! Cocoa is the best dog!')

# num = 100

# while num > 10:
#     print(num)
#     num -= 5

# for num in range(100, 1, -2):
#     print(num)

# str = 'adfasdasdfasf'
# for letter in str:
#     print(letter, end='')

weapons = ['Gun', 'Knife', 'Rock']
weapon = input('What weapon do you chose? ')

while weapon.capitalize() not in weapons:
    print('wrong')
    weapon = input('What weapon do you chose? ')
