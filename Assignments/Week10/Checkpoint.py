shopping_list = []

# create a function to print a sorted list


def print_nicely():
    print()
    for i, item in enumerate(sorted_list):
        print(f'{i}. {item}')
    print()


# append to the list with a while loop
end = ''

while end != 'quit':
    item = input(
        'What item would you like to add to your shopping list?\n')
    if item in shopping_list:
        print(f'You already added {item}')
    else:
        shopping_list.append(item)
    sorted_list = sorted(shopping_list)

    print_nicely()

    end = input(
        'Enter quit if you want to exit. Press "Enter" to continue.').lower()

change = True

while change:
    change = input(
        'Would you like to update an item on the list? (Y/N)').upper()
    if change == 'Y':
        change == True
    else:
        change == False

    if change == 'Y':
        user_choice = int(
            input('What is the number of the item you wish to change? '))
        new_item = input('What is the new item? ')
        sorted_list[user_choice] = new_item
    else:
        change = False

print_nicely()
