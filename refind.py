import re

# Input string
s = input()

# Regular expression to match only vowels surrounded by consonants
# We make sure the vowels are surrounded by consonants (or the start/end of the string)
matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]+(?=[^aeiouAEIOU])', s)

# If matches are found, print each one. If no matches, print -1.
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
