#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Find the common prefix length
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    
    # Calculate operations needed: deletions from s + additions for t
    min_operations = len(s) - common_length + len(t) - common_length
    
    # Case 1: If k is exactly equal to min_operations, we can do it
    if k == min_operations:
        return "Yes"
    
    # Case 2: If k > min_operations but we can delete everything and start over
    if k >= len(s) + len(t):
        return "Yes"
    
    # Case 3: If k > min_operations and the extra operations are even
    # (we can delete and add back the same characters)
    if k > min_operations and (k - min_operations) % 2 == 0:
        return "Yes"
    
    # Case 4: Special case - if we can delete past the common prefix
    # and start building from an earlier point
    total_deletions_possible = len(s)
    remaining_after_deletions = k - total_deletions_possible
    
    if remaining_after_deletions >= 0 and remaining_after_deletions >= len(t):
        return "Yes"
    
    # If none of the above cases apply, it's not possible
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()