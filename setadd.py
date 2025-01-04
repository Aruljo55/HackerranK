# Input parsing
n = int(input())  # The number of country stamps
countries = set()  # Initialize an empty set

# Loop to add each country to the set
for _ in range(n):
    country = input()  # Read country name
    countries.add(country)  # Add the country to the set

# Output the number of distinct countries
print(len(countries))
