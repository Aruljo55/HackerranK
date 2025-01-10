import re

def validate_mobile_numbers():
    # Read the number of inputs
    n = int(input())  # The number of mobile numbers
    
    # Regular expression pattern for a valid mobile number
    pattern = r'^[789]\d{9}$'
    
    # Process each mobile number
    for _ in range(n):
        # Read the mobile number as a string
        mobile_number = input().strip()
        
        # Check if the mobile number matches the regular expression
        if re.match(pattern, mobile_number):
            print("YES")
        else:
            print("NO")

# Example usage
validate_mobile_numbers()
