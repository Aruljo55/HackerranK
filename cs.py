import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    """
    Cuts the sticks iteratively, discarding the shortest pieces until none left.
    
    Parameters:
    arr (list): array of stick lengths
    
    Returns:
    list: number of sticks before each cut operation
    """
    result = []
    
    # Continue until all sticks are removed
    while arr:
        # Count how many sticks we have before cutting
        result.append(len(arr))
        
        # Find the length of the shortest stick
        min_length = min(arr)
        
        # Cut each stick by min_length and keep only the ones with positive length
        new_arr = []
        for stick in arr:
            remaining = stick - min_length
            if remaining > 0:
                new_arr.append(remaining)
        
        # Update arr with the remaining sticks
        arr = new_arr
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
