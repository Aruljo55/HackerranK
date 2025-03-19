#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Calculate turns from front
    # Integer division by 2 works because:
    # - Page 1 requires 0 turns
    # - Pages 2-3 require 1 turn
    # - Pages 4-5 require 2 turns, etc.
    front_turns = p // 2
    
    # Calculate turns from back
    # For even n, the last page is alone
    # For odd n, the last page shares a spread with the second-to-last page
    back_turns = n // 2 - p // 2
    
    # Return minimum of turns from front or back
    return min(front_turns, back_turns)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()c