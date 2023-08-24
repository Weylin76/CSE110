kids = ['Katelyn', 'Ethan', 'Bryce', 'Cocoa', 'Cheaters']

lst = [kid for kid in kids]
print(lst)

letter = [kid[0].lower() for kid in kids]
print(letter)

fav_kid = [kid for kid in kids if kid[0].upper() == 'C']
print(fav_kid)

not_fav_kids = [kid for kid in kids if kid not in ['Cocoa']]
print(not_fav_kids)

numbers = [1, 2, 3, 4, 5]
doubled_nums = [doubled*2 for doubled in numbers]
print(doubled_nums)

if_list = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(if_list)

# Print a list of all numbers from 1 - 100 that are evenly divisible by 12 (12, 24, etc)
divisible_nums = [num for num in range(1, 101) if num % 12 == 0]
print(divisible_nums)

# print out the non-vowels in the word amazing
word = [letter for letter in 'amazing' if letter.lower() not in 'aeiou']
print(word)
