import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    special_count = 0
    page = 1

    for chapter in arr:
        for problem in range(1, chapter + 1):
            if problem == page:
                special_count += 1
            if problem % k == 0 or problem == chapter:
                page += 1

    return special_count


    for chapter in arr:
        for problem in range(1, chapter + 1):
            if problem == page:
                special_count += 1
            if problem % k == 0 or problem == chapter:
                page += 1

    return special_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
