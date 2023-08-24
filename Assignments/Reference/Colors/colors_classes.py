class Colors:
    RESET = '\033[0m'

    class Regular:
        BLACK = '\033[0;30m'
        RED = '\033[0;31m'
        GREEN = '\033[0;32m'
        YELLOW = '\033[0;33m'
        BLUE = '\033[0;34m'
        MAGENTA = '\033[0;35m'
        CYAN = '\033[0;36m'
        WHITE = '\033[0;37m'

    class Bold:
        BLACK = '\033[1;30m'
        RED = '\033[1;31m'
        GREEN = '\033[1;32m'
        YELLOW = '\033[1;33m'
        BLUE = '\033[1;34m'
        MAGENTA = '\033[1;35m'
        CYAN = '\033[1;36m'
        WHITE = '\033[1;37m'

    class Underline:
        BLACK = '\033[4;30m'
        RED = '\033[4;31m'
        GREEN = '\033[4;32m'
        YELLOW = '\033[4;33m'
        BLUE = '\033[4;34m'
        MAGENTA = '\033[4;35m'
        CYAN = '\033[4;36m'
        WHITE = '\033[4;37m'

    class Background:
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        YELLOW = '\033[43m'
        BLUE = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN = '\033[46m'
        WHITE = '\033[47m'


# Example usage
print(Colors.Regular.BLACK + 'Black' + Colors.RESET)
print(Colors.Regular.RED + 'Red' + Colors.RESET)
print(Colors.Regular.GREEN + 'Green' + Colors.RESET)
print(Colors.Regular.YELLOW + 'Yellow' + Colors.RESET)
print(Colors.Regular.BLUE + 'Blue' + Colors.RESET)
print(Colors.Regular.MAGENTA + 'Magenta' + Colors.RESET)
print(Colors.Regular.CYAN + 'Cyan' + Colors.RESET)
print(Colors.Regular.WHITE + 'White' + Colors.RESET)
