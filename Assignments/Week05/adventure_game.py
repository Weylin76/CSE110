# Create an adventure game with multiple levels of if/elif/else statements

# Allow program to display colors:
class Colors:
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    RESET = '\033[0m'


# Define possible choices
user_choice = ''

# Create the story for the adventure game
user_choice = input('Choose the mode of transportation you wish to use: ' +
                    Colors.MAGENTA + '1. BOAT 2. CAR 3. ATV ' + Colors.RESET)
try:
    # Boat option
    if user_choice == '1':
        user_choice = input('Do you want to take the boat on the: ' +
                            Colors.MAGENTA + '1. RIVER 2. STREAM 3. LAKE: ' + Colors.RESET)

        # River
        if user_choice == '1':
            user_choice = input('Do you want to go: ' + Colors.MAGENTA +
                                '1. FAST 2. SLOW ' + Colors.RESET)
            if user_choice == '1':
                print(
                    Colors.GREEN + '\nYou had a fun adventure and outran all the bears!\n' + Colors.RESET)
            elif user_choice == '2':
                print(
                    Colors.RED + '\nBoring choice, your boat sunk and you died!\n' + Colors.RESET)
            else:
                print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

        # Stream Option
        elif user_choice == '2':
            user_choice = input('Do you want to go fishing? ' +
                                Colors.MAGENTA + '1. YES 2. NO ' + Colors.RESET)
            if user_choice == '1':
                print(Colors.GREEN +
                      '\nNice choice, you caught a lot of fish!\n' + Colors.RESET)
            else:
                print(Colors.RED + '\nYou were eaten by an ALLIGATOR!\n' + Colors.RESET)

        # Lake Option
        elif user_choice == '3':
            user_choice = input('Do you want to go fishing? ' +
                                Colors.MAGENTA + '1. YES 2. NO ' + Colors.RESET)
            if user_choice == '1':
                print(Colors.GREEN +
                      '\nNice choice, you will be eating well tonight!\n' + Colors.RESET)
            else:
                print(Colors.RED +
                      '\nYou fell out of the boat and died!\n' + Colors.RESET)

        # kill user for invalid option
        else:
            print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

    # Car option
    elif user_choice == '2':
        user_choice = input('Do you want to drive to: ' + Colors.MAGENTA +
                            '1. A DIFFERENT CAMPSITE 2. UP THE MOUNTAIN 3. HOME? ' + Colors.RESET)

        # A different campsite option
        if user_choice == '1':
            user_choice = input('Do you want to go: ' + Colors.MAGENTA +
                                '1. Close 2. Far away ' + Colors.RESET)
            if user_choice == '1':
                print(
                    Colors.RED + '\nYou went to a killer campsite. Better luck next time!\n' + Colors.RESET)
            elif user_choice == '2':
                print(
                    Colors.RED + '\nYou ran out of gas and died!\n' + Colors.RESET)
            else:
                print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

        # Up the mountain option
        elif user_choice == '2':
            user_choice = input('Do you want to climb the mountain? ' +
                                Colors.MAGENTA + '1. YES 2. NO ' + Colors.RESET)
            if user_choice == '1':
                print(Colors.GREEN +
                      '\nYou had a great time on your 4-wheeling adventure!\n' + Colors.RESET)
            elif user_choice == '2':
                print(
                    Colors.GREEN + '\nYou took some great pictures of the mountain!\n' + Colors.RESET)
            else:
                print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

        # Home Option
        else:
            print(Colors.RED + 'Never choose home, you die!' + Colors.RESET)

    # ATV option
    elif user_choice == '3':
        user_choice = input('Do you want to go on the: ' +
                            Colors.MAGENTA + '1. TRAILS 2. ROAD ' + Colors.RESET)
        if user_choice == '1':
            input(Colors.GREEN + 'You had a great time!\n' + Colors.RESET)
        elif user_choice == '2':
            print(
                Colors.RED + 'Boring Choice! You were hit and killed by another car!\n' + Colors.RESET)
        else:
            print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

    # Kill user for invalid selecton
    else:
        print(Colors.RED + 'Invalid option.  YOU DIE!!' + Colors.RESET)

except Exception:
    print('Invalid option.  YOU DIE!!.')
