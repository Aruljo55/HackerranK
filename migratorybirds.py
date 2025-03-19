#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Create a frequency counter for each bird type
    # Since bird types are guaranteed to be 1-5, we can use a simple array
    bird_counts = [0] * 6  # Index 0 will be unused
    
    # Count the frequency of each bird type
    for bird_type in arr:
        bird_counts[bird_type] += 1
    
    # Find the maximum frequency
    max_count = 0
    most_frequent_type = 0
    
    # Iterate through the bird types (1-5)
    # Since we're iterating in ascending order, if there's a tie,
    # we'll automatically choose the smallest bird type ID
    for bird_type in range(1, 6):
        if bird_counts[bird_type] > max_count:
            max_count = bird_counts[bird_type]
            most_frequent_type = bird_type
    
    return most_frequent_type

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()