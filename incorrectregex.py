import re

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input().strip()
    try:
        # Try compiling the string into a regex pattern
        re.compile(s)
        print("True")
    except re.error:
        # If there is an error in regex compilation, it's invalid
        print("False")
