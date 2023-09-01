master_list = []
line_level_list = []
newest_list = []
min_age = 999
min_age_year = 0
min_age_country = ""  # Variable to store the country with min age
max_age = 0
max_age_year = 0
max_age_country = ""  # Variable to store the country with max age


with open('life-expectancy.csv') as life:
    header = next(life)  # Read and skip the header line

    for line in life:
        line = line.strip()
        parts = line.split(",")
        master_list.append(line)
        country = parts[0]
        acronym = parts[1]
        year = int(parts[2])  # year as a int
        age = float(parts[3])  # Age as a float

        if age < min_age:
            min_age = age
            min_age_country = country
            min_age_year = year

        if age > max_age:
            max_age = age
            max_age_country = country
            max_age_year = year

print(f'Max Age: {min_age} Country: {min_age_country} year: {min_age_year}')
print(f'Max Age: {max_age} Country: {max_age_country} year: {max_age_year}')
