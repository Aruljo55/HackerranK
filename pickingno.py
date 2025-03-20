import math
import os
import random
import re
import sys
def pickingNumbers(a):
    # Count the frequency of each number
    frequency = {}
    for num in a:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the longest valid subarray
    max_length = 0
    
    # Sort the keys to make it easier to find adjacent numbers
    sorted_keys = sorted(frequency.keys())
    
    # Check the length of each possible subarray with difference <= 1
    for i in range(len(sorted_keys)):
        # Option 1: Just the current number by itself
        max_length = max(max_length, frequency[sorted_keys[i]])
        
        # Option 2: Current number and the next number (if their difference is <= 1)
        if i + 1 < len(sorted_keys) and sorted_keys[i+1] - sorted_keys[i] <= 1:
            max_length = max(max_length, frequency[sorted_keys[i]] + frequency[sorted_keys[i+1]])
    
    return max_length
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
