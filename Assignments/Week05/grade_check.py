print()  # print blank line
# validate that the user can only enter a float
while True:
    try:
        grade = float(input('What is the percent you recieved? '))
        break
    except ValueError:
        print('please only enter a number for the percent!')

# caluclate the letter grade value
letter_grade = ''
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# step 2 - Determine if grade is passing
if letter_grade.upper() in ('A', 'B', 'C'):
    print(f'Congrats you are passing with a letter grade of {letter_grade}!')
else:
    print('You are close, keep working hard to get there!')
print()  # print blank line

# STRETCH CHALLENGE
grade_sign = ''

if grade % 10 >= 7:
    grade_sign = '+'
elif grade % 10 <= 3:
    grade_sign = '-'

# disable A+. F+, and F-
if letter_grade == 'A' and grade_sign == '+':
    grade_sign = ''
elif letter_grade == 'F':
    grade_sign = ''

print(f'Final grade: \n{letter_grade}{grade_sign}\n')
