# Load the dataset in your Python program
master_list = []

with open('life-expectancy.csv') as life:
    header = next(life)  # Read and skip the header line

    for line in life:
        line = line.strip()
        parts = line.split(",")
        master_list.append(parts)

# Get user input for the year of interest
user_year = int(input("Enter the year of interest: "))

# Find the overall max and min life expectancy and corresponding years
overall_max_life = float('-inf')
overall_max_country = ""
overall_max_year = 0
overall_min_life = float('inf')
overall_min_country = ""
overall_min_year = 0

for row in master_list:
    country = row[0]
    year = int(row[2])
    life_expectancy = float(row[3])

    if life_expectancy > overall_max_life:
        overall_max_life = life_expectancy
        overall_max_country = country
        overall_max_year = year

    if life_expectancy < overall_min_life:
        overall_min_life = life_expectancy
        overall_min_country = country
        overall_min_year = year

print(
    f"The overall max life expectancy is: {overall_max_life:.3f} from {overall_max_country} in {overall_max_year}")
print(
    f"The overall min life expectancy is: {overall_min_life:.3f} from {overall_min_country} in {overall_min_year}")

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
