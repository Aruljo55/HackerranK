import re

# Regular expression for range [100000, 999999]
regex_integer_in_range = r"^[1-9][0-9]{5}$"

# Regular expression to find alternating repetitive digit pairs
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

# Sample input
P = input().strip()

# Check the postal code validity
is_valid = (bool(re.match(regex_integer_in_range, P)) and
            len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

print(is_valid)
