import re

def find_repeating_character(s):
    # Search for a repeating alphanumeric character
    match = re.search(r'([a-zA-Z0-9])\1', s)
    
    if match:
        print(match.group(1))  # Print the first repeating alphanumeric character
    else:
        print(-1)  # If no repeating character is found, print -1

# Input
string = input().strip()

# Calling the function
find_repeating_character(string)
