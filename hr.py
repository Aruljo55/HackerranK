import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#
def hurdleRace(k, height):
    # Find the maximum hurdle height
    max_height = max(height)
    
    # Calculate how many doses are needed
    # If the character can already jump higher than all hurdles, return 0
    if k >= max_height:
        return 0
    # Otherwise, return the difference between max hurdle height and jump height
    else:
        return max_height - k
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
