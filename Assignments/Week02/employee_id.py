# Create a list of varibles for the employee badge:
first_name = input('Enter your first name: ').strip()
last_name = input('Enter your last name: ').strip()
phone = input('Enter your phone number with area code: ').strip()
email = input('Enter your email address: ').strip()
emp_id = input('Enter your employee ID: ').strip()
job_title = input('Enter your job title: ').strip()

# Reference Colors:
'''
Black: "\033[0;30m"
Red: "\033[0;31m"
Green: "\033[0;32m"
Yellow: "\033[0;33m"
Blue: "\033[0;34m"
Magenta: "\033[0;35m"
Cyan: "\033[0;36m"
White: "\033[0;37m"
'''

# Define colors to use with employee badge
blue = "\033[0;34m"
green = "\033[0;32m"
white = "\033[0;37m"
line = '-'*40

# Print blue lines for managers otherwise green for everyone else
if 'Manage' in job_title.capitalize():
    color = blue
else:
    color = green

# print out the badge card
print()
print('Employee Badge Information'.center(40))
print(color + line + white)
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print(f'ID: {emp_id[:2]}-{emp_id[2:]} ')
print()
print(email.lower())
print(f"({phone[:3]}) {phone[3:6]}-{phone[6:]}")
print(color + line + white)
print()
