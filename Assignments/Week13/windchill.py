import sys
while True:
    temp_input = input("What is the temperature? ")

    if temp_input.lstrip('-').isdigit():  # Allow a minus sign at the beginning
        temp = float(temp_input)
        break  # Exit the loop if input is a valid number
    else:
        print("Invalid input. Please enter a valid number for the temperature.")

degree_type = input('Fahrenheit or Celsius (F/C): ')

if degree_type.upper() == 'F':
    T = temp
elif degree_type.upper() == 'C':
    T = 1.8 * temp + 32
else:
    print('You entered an invalid selection.')
    sys.exit(1)  # Exit the program with an error code

for V in range(5, 61, 5):
    wind_chill = (35.74 + 0.6215 * T - 35.75 *
                  (V**0.16) + 0.4275 * T * (V**0.16))
    print(
        f'At temperature {T}F, and wind speed {V} mph, the wind chill is: {wind_chill:.2f}F')
