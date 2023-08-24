#get 3 varibles from the user
age = int(input('How old are you? '))
cartons = int(input('How many cartons of eggs do you have? '))
cookies = int(input('How many cookies do you have? '))
num_of_ppl = int(input('How many people will be eating cookies? '))

#perform required calculations
print()
print(f'You will be {age + 1} on your next birthday!')
print()
print(f'You have a total of {cartons * 12} eggs!')
print()
print(f'You have {cookies / num_of_ppl:.2f} cookies each!')
print()