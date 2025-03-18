#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize variables to track min and max scores
    min_score = scores[0]
    max_score = scores[0]
    
    # Initialize counters for breaking records
    min_breaks = 0
    max_breaks = 0
    
    # Iterate through the scores starting from the second game
    for score in scores[1:]:
        # Check if current score breaks the maximum record
        if score > max_score:
            max_score = score
            max_breaks += 1
        # Check if current score breaks the minimum record
        elif score < min_score:
            min_score = score
            min_breaks += 1
    
    # Return the counts as an array [max_breaks, min_breaks]
    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()