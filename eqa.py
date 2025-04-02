import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    """
    Determine the minimum number of elements to delete to leave only elements of equal value
    
    Parameters:
    arr (list): an array of integers
    
    Returns:
    int: the minimum number of deletions required
    """
    # Count occurrences of each element
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the most frequent element
    max_frequency = max(frequency.values())
    
    # Calculate minimum deletions (total elements - most frequent element count)
    min_deletions = len(arr) - max_frequency
    
    return min_deletions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
