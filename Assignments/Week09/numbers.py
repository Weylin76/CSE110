number_list = []
more_nums = ''

while more_nums != 'N':
    num = int(input('Enter a number to the list: '))
    number_list.append(num)

    more_nums = input(
        'Do you want to add another number to the list? (Y/N)').upper()
print(number_list)

positive_nums = []
negative_nums = []
for num in number_list:
    if num >= 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

for num in positive_nums:
    smallest_pos = min(positive_nums)

for num in negative_nums:
    smallest_neg = min(negative_nums)

print(smallest_neg)

sum_nums = sum(number_list)
average_nums = sum_nums/len(number_list)
max_num = max(number_list)
min_num = min(number_list)
sorted_nums = sorted(number_list)

print(
    f'\nMax: {max_num:,}\nMin: {min_num:,}\nAverage:{average_nums:,.2f}\nSum:{sum_nums:,}\nSmallest Positive Number:{smallest_pos:,}\nSmallest Negative Number:{smallest_neg:,}\n')
print(sorted_nums)
