# convert from temp Fahrenheit to Celsius
fah = float(input('What is the temperature in Fahrenheit? '))

# formula to convert
cel = (fah-32) * (5/9)

# print in Celsius
print(f'The current temperature is {cel:.1f} °C!')
