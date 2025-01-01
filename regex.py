import re

# Read the number of lines
n = int(input())

# Function to replace && and || with and/or in the correct format
def replace_symbols(text):
    # Replace '&&' with 'and' and '||' with 'or' only if surrounded by spaces
    text = re.sub(r'(?<= )&&(?= )', 'and', text)
    text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
    return text

# Process each line of the input
for _ in range(n):
    line = input()  # Read each line
    print(replace_symbols(line))  # Modify and print the line
