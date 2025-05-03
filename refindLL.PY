import re

s = input()

# regex: consonant + group of >=2 vowels + consonant
matches = re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])', s, flags=re.I)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
