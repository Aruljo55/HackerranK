import re

# Read input values
s = input()  # Main string
sub = input()  # Substring to find

# Start the search from the beginning of the string
start = 0
matches = []

while start < len(s):
    # Search for the substring starting from the current index
    m = re.search(sub, s[start:])
    if m:
        # Adjust the match indices to account for the start of the string
        matches.append((start + m.start(), start + m.end() - 1))
        # Move the start index to just after the current match to find overlapping matches
        start += m.start() + 1
    else:
        break

# If no matches were found, print (-1, -1)
if not matches:
    print((-1, -1))
else:
    for match in matches:
        print(match)
