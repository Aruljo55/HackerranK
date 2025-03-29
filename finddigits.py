#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Convert n to a string to iterate through its digits
    n_str = str(n)
    
    # Initialize count of divisors
    count = 0
    
    # Check each digit
    for digit in n_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        
        # Skip if the digit is 0 (division by zero is undefined)
        if digit_int == 0:
            continue
        
        # Check if n is divisible by the digit
        if n % digit_int == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()