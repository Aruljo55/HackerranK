import math
import os
import random
import re
import sys

def permutationEquation(p):
    # Create a position map for faster lookups
    # This maps the value to its position (1-indexed)
    position = {}
    for i in range(len(p)):
        position[p[i]] = i + 1
    
    result = []
    
    # For each value x from 1 to n
    for x in range(1, len(p) + 1):
        # Find position of x in p: position[x]
        # Find position of position[x] in p: position[position[x]]
        # Add to result
        result.append(position[position[x]])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
