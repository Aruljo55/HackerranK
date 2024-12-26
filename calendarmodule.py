import calendar

# Input: month, day, year as space-separated integers
month, day, year = map(int, input().split())

# Get the day of the week (0=Monday, 6=Sunday)
day_of_week = calendar.weekday(year, month, day)

# Convert day of the week to its name in uppercase
day_name = calendar.day_name[day_of_week].upper()

# Output the result
print(day_name)
