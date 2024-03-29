master_list = []
min_age = 999
min_age_year = 0
min_age_country = ""  # Variable to store the country with min age
max_age = 0
max_age_year = 0
max_age_country = ""  # Variable to store the country with max age

# varialbes for user search
user_min_age = 999
user_min_county = ''
user_min_age_year = 9999

user_year = int(input("Enter the year of interest: "))


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

# Find and display information for the user's specified year
total_life_expectancy = 0
num_countries = 0
max_life_expectancy = float('-inf')
max_country = ""
min_life_expectancy = float('inf')
min_country = ""

for row in master_list:
    year = int(row[2])
    if year == user_year:
        life_expectancy = float(row[3])

        total_life_expectancy += life_expectancy
        num_countries += 1

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = row[0]

        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = row[0]

average_life_expectancy = total_life_expectancy / num_countries

print(f"\nFor the year {user_year}:")
print(
    f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
print(
    f"The max life expectancy was in {max_country} with {max_life_expectancy:.2f}")
print(
    f"The min life expectancy was in {min_country} with {min_life_expectancy:.3f}")

print(f'Max Age: {min_age} Country: {min_age_country} year: {min_age_year}')
print(f'Max Age: {max_age} Country: {max_age_country} year: {max_age_year}')
