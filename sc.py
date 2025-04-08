import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    cycle_start = 1
    cycle_value = 3

    while t > cycle_start + cycle_value - 1:
        cycle_start += cycle_value
        cycle_value *= 2

    return cycle_value - (t - cycle_start)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
