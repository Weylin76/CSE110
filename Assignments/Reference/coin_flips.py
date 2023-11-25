import random

flips = []
for i in range(1000):
    if random.randint(0, 1) == 0:
        flips.append('heads')
    else:
        flips.append('tails')

max_consecutive = 0
current_consecutive = 1

for i in range(1, len(flips)):
    if flips[i] == flips[i - 1]:
        current_consecutive += 1
    else:
        current_consecutive = 1

    if current_consecutive > max_consecutive:
        max_consecutive = current_consecutive

print(f'Highest number of consecutive identical outcomes: {max_consecutive}')
