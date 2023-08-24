# you can validate string to ensure good data quality

# Example cannot be empty
import re
while True:
    string = input("Enter a string: ")

    if string:  # Check if the input string is non-empty
        break  # Exit the loop if a non-empty string is entered
    else:
        print("Invalid input. Please enter a non-empty string.")

print("Valid string:", string)

# Example is alpha
while True:
    string = input("Enter an alphabetic string: ")

    if string.isalpha():  # Check if the input string consists only of alphabetic characters
        break  # Exit the loop if a valid alphabetic string is entered
    else:
        print("Invalid input. Please enter an alphabetic string.")

print("Valid alphabetic string:", string)

# Example Validating Specific String Format
while True:
    string = input("Enter a string in the format 'AAXXXX': ")

    if len(string) == 6 and string[0:2].isalpha() and string[2:].isdigit():
        break  # Exit the loop if a string in the specified format is entered
    else:
        print("Invalid input. Please enter a string in the format 'AAXXXX'.")

print("Valid string:", string)

# Example regular expressions to validate a string input
'''
In this example, the loop continues until the user enters a valid alphabetic string. 
The regular expression pattern r'^[a-zA-Z]+$' matches a string that consists only of
uppercase or lowercase alphabetic characters. If the entered string matches the pattern, 
the loop is exited; otherwise, an error message is displayed, and the loop repeats until 
a valid input is provided.
'''

while True:
    string = input("Enter a string: ")
    pattern = r'^[a-zA-Z]+$'

    if re.match(pattern, string):
        break  # Exit the loop if a valid alphabetic string is entered
    else:
        print("Invalid input. Please enter an alphabetic string.")

print("Valid string:", string)

# Example validates a string input based on specific conditions
'''
In this example, the loop continues until the user enters a valid 
string based on the specified conditions. The conditions are:

The string length should be greater than or equal to 5.
The string should consist only of lowercase alphabetic characters.
If the entered string satisfies these conditions, the loop is exited; 
otherwise, an error message is displayed, and the loop repeats until 
a valid input is provided.
'''
while True:
    string = input("Enter a string: ")

    if len(string) >= 5 and string.islower() and string.isalpha():
        break  # Exit the loop if a valid string is entered
    else:
        print("Invalid input. Please enter a lowercase alphabetic string with at least 5 characters.")

print("Valid string:", string)
