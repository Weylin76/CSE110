friends_list = []
add_more = ''

while add_more != 'N':
    friend = input('What is a name of your friend?\n').capitalize()
    friends_list.append(friend)
    add_more = input(
        'Would you like to add another friend to your list? (Y/N)').upper()
