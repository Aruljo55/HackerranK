import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    """
    Determine the minimum number of jumps needed to win the cloud game
    
    Parameters:
    c (list): Array of cloud types (0 for safe, 1 for thunderheads)
    
    Returns:
    int: The minimum number of jumps required
    """
    position = 0
    jumps = 0
    n = len(c)
    
    # Continue until we reach the last cloud
    while position < n - 1:
        # Always try to jump 2 clouds if possible
        if position + 2 < n and c[position + 2] == 0:
            position += 2
        else:
            # Otherwise jump 1 cloud
            position += 1
        
        jumps += 1
    
    return jumps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
