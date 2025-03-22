import math
import os
import random
import re
import sys

def utopianTree(n):
    # Initial height of the tree
    height = 1
    
    # Iterate through each growth cycle
    for i in range(n):
        # Spring: height doubles
        if i % 2 == 0:
            height *= 2
        # Summer: height increases by 1
        else:
            height += 1
    
    return height
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
