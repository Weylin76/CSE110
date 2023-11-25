# create a color library
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"


# create variables to capture user input
print()
kids_meal_price = float(input(Color.BLUE + "What is the kid's meal price? "))
adult_meal_price = float(
    input('What is the price of the adult meal? '))
num_of_kids = int(input(Color.YELLOW + 'How many children are there? '))
num_of_adults = int(input('How many adults are there? '))
sales_tax_rate = float(
    input(Color.GREEN + 'What is the sale tax rate? '))

# create calculated variables
subtotal = (kids_meal_price * num_of_kids) + (adult_meal_price * num_of_adults)
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax

# create print statement
print()
print(Color.RESET + f'Subtotal \t${subtotal:.2f}')
print(f'Sales Tax: \t${sales_tax:.2f}')
print(f'Total \t\t${total:,.2f}')

# create a variable for payment
payment_amt = float(input('How much is the payment amount? '))

# create a payment check to ensure proper payment is collected

while payment_amt < total:
    print(Color.RED + f'Insufficent amount given, please pay a higer amount!' + Color.RESET)
    print(f'Your total was ${total:.2f}.')
    payment_amt = float(input('How much is the payment amount? '))

# create and print change and thank you message
customer_change = payment_amt - total
print()
print(Color.MAGENTA +
      'Thank you for visiting us.  Your change is ' + Color.GREEN +
      f'${customer_change:.2f}.' + Color.MAGENTA + '\nPlease visit us again!'
      + Color.RESET)
print()
