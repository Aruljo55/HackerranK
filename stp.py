import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    # Calculate the position of the last sweet
    # We need to take into account the starting position (s)
    # and the number of prisoners (n)
    
    # Calculate the final position
    # (s-1) shifts the starting position to 0-indexed
    # (m-1) accounts for the fact that we're looking for the position after (m-1) candies
    # % n ensures we wrap around the circle correctly
    # +1 shifts back to 1-indexed
    final_position = ((s - 1) + (m - 1)) % n + 1
    
    return final_position
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
