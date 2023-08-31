age_list = []
max_age = 0
min_age = 999

with open('life-expectancy.csv') as life:
    header = next(life)  # Read and skip the header line

    for line in life:
        line = line.strip()
        parts = line.split(",")
        country = parts[0]
        acronym = parts[1]
        year = int(parts[2])  # year as a int
        age = float(parts[3])  # Age as a float

        age_list.append(age)


for age in age_list:
    if age > max_age:
        max_age = age

for age in age_list:
    if age < min_age:
        min_age = age

print(max_age)
print(min_age)
