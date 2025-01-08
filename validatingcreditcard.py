import re

def is_valid_card(card):
    # Remove hyphens for easier processing
    card_no_hyphens = card.replace('-', '')

    # Check if card contains only digits and has exactly 16 characters
    if not re.fullmatch(r'\d{16}', card_no_hyphens):
        return "Invalid"
    
    # Check if card starts with 4, 5, or 6
    if not card_no_hyphens[0] in "456":
        return "Invalid"
    
    # Check if it contains 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_no_hyphens):
        return "Invalid"
    
    # If hyphens are present, check proper grouping
    if '-' in card:
        if not re.fullmatch(r'(\d{4}-){3}\d{4}', card):
            return "Invalid"
    
    # If all checks passed
    return "Valid"

# Input reading
n = int(input())  # Number of credit card numbers
cards = [input().strip() for _ in range(n)]

# Validate each card and print the result
for card in cards:
    print(is_valid_card(card))
