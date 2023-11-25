import random

sums_list = []

# Repeat the process of rolling the dice 100 times, 100 times
for i in range(100):
    roll_sum = 0
    for j in range(100):
        roll = random.randint(1, 6)
        roll_sum += roll
    sums_list.append(roll_sum)

roll_min = min(sums_list)
roll_max = max(sums_list)
roll_average = sum(sums_list) / len(sums_list)  # Calculating the average

print(f'min: {roll_min}, max: {roll_max}, average: {roll_average}')
