import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    count = 0
    if not re.search(r'[0-9]', password):
        count += 1
    if not re.search(r'[a-z]', password):
        count += 1
    if not re.search(r'[A-Z]', password):
        count += 1
    if not re.search(r'[!@#$%^&*()\-+]', password):
        count += 1
    return max(count, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
