import re
import email.utils

def validate_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{2,4}$'
    return re.match(pattern, email) is not None

def main():
    # Read the number of email address inputs
    n = int(input())
    
    # Process each name and email pair
    for _ in range(n):
        # Read name and email pair
        name, email = input().split(' <')
        email = email.rstrip('>')  # Remove the '>' at the end of the email
        
        # Validate the email
        if validate_email(email):
            print(f"{name} <{email}>")

# Example usage
main()
