import math


def square_area(side):
    return side*side


def rect_area(len, width):
    return len * width


def circle_area(radius):
    return math.pi*(radius**2)


user_input = ''
value = 0.0
width = 0.0
while user_input != 'quit':
    user_input = input(
        'What shape do you wish to calculate the area of: (square, rectangle, circle)\n')
    if user_input.lower() == 'square':
        value = float(input('What is the length of the side of the square?\n'))
        print(square_area(value))
    elif user_input.lower() == 'rectangle':
        value = float(input('What is the length?\n'))
        width = float(input('What is the width?\n'))
        print(rect_area(value, width))
    elif user_input.lower() == 'circle':
        value = float(input('What is the radius?\n'))
        print(circle_area(value))
