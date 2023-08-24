'''
v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

Where:

m = mass (in kg)

g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)

t = time (in seconds)

c = 1/2 p A C

p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)

A = cross sectional area of projectile (in square meters)

C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)

exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

'''

# Testing example
'''
Welcome to the velocity calculator. Please enter the following:

Mass (in kg): 5
Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
Time (in seconds): 10
Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
Cross sectional area (in m^2): 0.01
Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5

The inner value of c is: 0.003
The velocity after 10.0 seconds is: 67.512 m/s

'''

# Import the Math library

# define the varibles for the calculation
import math
m = float(input('Enter the mass in KG: '))
g = float(input('Enter the acceleration due to gravity: '))
t = float(input('Enter the time in seconds: '))
p = float(input('Enter in the density of fluid: '))
A = float(input('Enter in the cross sectional area of projectile: '))
C = float(input('Enter in the drag constant: '))
c = .5 * p * A * C

# The formula for the calculation
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Print out the answer:
print()
print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after {t:.1f} is: {v:.3f} m/s')
print()
