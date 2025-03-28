#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    # Calculate LCM of array a
    lcm_result = a[0]
    for i in range(1, len(a)):
        lcm_result = lcm(lcm_result, a[i])
    
    # Calculate GCD of array b
    gcd_result = b[0]
    for i in range(1, len(b)):
        gcd_result = gcd(gcd_result, b[i])
    
    # Count valid integers
    count = 0
    multiple = lcm_result
    
    while multiple <= gcd_result:
        if gcd_result % multiple == 0:
            count += 1
        multiple += lcm_result
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()