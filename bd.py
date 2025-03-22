import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    # Count of beautiful days
    beautiful_count = 0
    
    # Check each day in the range
    for day in range(i, j + 1):
        # Convert the day to a string, reverse it, and convert back to integer
        day_reversed = int(str(day)[::-1])
        
        # Calculate the absolute difference
        difference = abs(day - day_reversed)
        
        # Check if the difference is evenly divisible by k
        if difference % k == 0:
            beautiful_count += 1
    
    return beautiful_count  
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
