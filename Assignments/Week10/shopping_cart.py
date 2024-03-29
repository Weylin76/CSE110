# Todo list
# 3. Validate only numbers can be enter for prices greater than 0 to 9999999999

# create color class
class Colors:
    RESET = '\033[0m'
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'


# create variables
shopping_list = []
item_price_list = []
action = ['add item', 'view cart', 'remove item', 'compute total', 'quit']
item = ''

# reuseable functions:


def print_full_list():
    print()
    if len(shopping_list) == 0:
        print(Colors.RED + 'Your Shopping cart is currently empty.')
    else:
        print('The contents of the shopping cart are:')
        for i, item in enumerate(shopping_list, start=1):
            item_price = item_price_list[i - 1]
            if i % 2 == 0:
                print(Colors.MAGENTA +
                      f'{i}. {item} - ${item_price:,.2f}' + Colors.RESET)
            else:
                print(Colors.CYAN +
                      f'{i}. {item} - ${item_price:,.2f}' + Colors.RESET)


print("\n\033[22;34;40m Welcome to the shopping center! \033[m")

# print('Welcome to the shopping center!')
while action != '5':
    print()

    action = input(Colors.RESET +
                   'What action would you like to take: \n'+Colors.YELLOW +
                   '1. Add Item\n'+Colors.CYAN +
                   '2. View Cart\n' + Colors.RED +
                   '3. Remove Item\n' + Colors.GREEN +
                   '4. Compute Total\n' + Colors.RESET +
                   '5. Quit\n\n')

    if action == '1':

        new_item = input('What item would you like to add?\n')
        item_price = float(input('What is the price of the item?\n'))
        while item_price <= 0 or item_price >= 999999999:
            print(Colors.RED + 'Sorry that price is not reasonable.' + Colors.RESET)
            item_price = float(input('What is the price of the item?\n'))
        if new_item.capitalize() in shopping_list:
            print(Colors.RED + '\nYou already have that item in your cart.')
        else:
            shopping_list.append(new_item.capitalize())
            item_price_list.append(item_price)
            print(Colors.BLUE +
                  f'\n{new_item.capitalize()} has been added to the list!')

    elif action == '2':
        print_full_list()

    elif action == '3':
        print_full_list()
        remove_index = int(
            input('What is the number of the item you wish to remove? '))
        if len(shopping_list) == 0:
            print(Colors.RED + '\nThere are no items in the cart!')
        else:
            removed_item = shopping_list.pop(remove_index-1)
            removed_price = item_price_list.pop(remove_index-1)
            print(Colors.RED +
                  f'{removed_item} has been remvoed!' + Colors.RESET)

    elif action == '4':
        total = sum(item_price_list)  # Using the sum() function
        print(Colors.GREEN + f'\nYour total is: ${total:,.2f}')
