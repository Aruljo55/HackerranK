import re

def is_valid_uid(uid):
    # Check if UID has exactly 10 characters
    if len(uid) != 10:
        return "Invalid"
    
    # Check if UID contains only alphanumeric characters
    if not uid.isalnum():
        return "Invalid"
    
    # Check if UID contains at least 2 uppercase letters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return "Invalid"
    
    # Check if UID contains at least 3 digits
    if len(re.findall(r'[0-9]', uid)) < 3:
        return "Invalid"
    
    # Check for uniqueness (no repeated characters)
    if len(set(uid)) != 10:
        return "Invalid"
    
    # All checks passed
    return "Valid"

# Input reading
n = int(input())  # Number of test cases
uids = [input().strip() for _ in range(n)]

# Validate each UID and print the result
for uid in uids:
    print(is_valid_uid(uid))
