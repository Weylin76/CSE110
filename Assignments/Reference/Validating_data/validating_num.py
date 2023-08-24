# You can validate numbers different ways from your user to ensure good data quality.
# importing regular expression for the last example
import re

# example 1
while True:
    try:
        num = int(input("Enter an integer: "))
        break  # Exit the loop if a valid integer is entered
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Valid integer:", num)

# example 2
while True:
    try:
        num = float(input("Enter a float: "))
        break  # Exit the loop if a valid float is entered
    except ValueError:
        print("Invalid input. Please enter a float.")

print("Valid float:", num)

# example 3
while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break  # Exit the loop if a valid positive integer is entered
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Valid positive integer:", num)

# example 4
while True:
    number = input("Enter a number: ")

    if number.isdigit():  # Check if the input is composed of digits
        break  # Exit the loop if a valid number is entered
    else:
        print("Invalid input. Please enter a number.")

print("Valid number:", number)

# example with regular expression
while True:
    phone_number = input("Enter a phone number (format: XXX-XXX-XXXX): ")
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    if re.match(pattern, phone_number):
        break  # Exit the loop if a valid phone number is entered
    else:
        print("Invalid phone number. Please enter in the format XXX-XXX-XXXX.")

print("Valid phone number:", phone_number)
