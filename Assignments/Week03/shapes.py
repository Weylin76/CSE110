#import the Math module
import math

#inputs from users
print()
square_len = int(input('Enter the length of a side of the square: '))
rec_len = int(input('Enter the length of the rectangle: '))
rec_width = int(input('Enter the width of the rectangle: '))
radius = int(input('Enter the radius of the circle: '))

#perform calculations
print()
print(f'The area of the square is {square_len **2}')
print(f'The area of the rectangle is {rec_len * rec_width}')
print(f'The area of the circle is {(radius**2)*math.pi:.2f}')
print()