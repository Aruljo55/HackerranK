import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    """
    Find the maximum size subset where no pair sums to a multiple of k
    
    Parameters:
    k (int): the divisor
    s (list): array of integers
    
    Returns:
    int: the maximum length of a valid subset
    """
    # Count remainders when divided by k
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1
    
    # Initialize with at most one number that is divisible by k
    max_size = min(remainder_count[0], 1)
    
    # For remainder pairs that sum to k
    for i in range(1, (k + 1) // 2):
        max_size += max(remainder_count[i], remainder_count[k - i])
    
    # For k being even, handle the special case of remainder k/2
    if k % 2 == 0:
        max_size += min(remainder_count[k // 2], 1)
    
    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
