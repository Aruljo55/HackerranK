import re

n = int(input())
lines = [input() for _ in range(n)]

inside_block = False
for line in lines:
    if '{' in line:
        inside_block = True
    if inside_block:
        matches = re.findall(r'#[0-9a-fA-F]{3}(?=[;,\s])|#[0-9a-fA-F]{6}(?=[;,\s])', line)
        for match in matches:
            print(match)
    if '}' in line:
        inside_block = False
