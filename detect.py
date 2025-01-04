import re

def is_valid_float(s):
    # Regular expression to check if the string represents a valid float
    pattern = r'^[+-]?(\d+\.\d*|\.\d+)$'
    if re.match(pattern, s):
        try:
            # Try to convert to float
            float(s)
            return True
        except ValueError:
            return False
    return False

# Input reading and processing
n = int(input())  # Number of test cases
for _ in range(n):
    s = input().strip()  # The string to check
    print(is_valid_float(s))
