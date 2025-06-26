import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    unique_chars = list(set(s))
    max_len = 0
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            filtered = [c for c in s if c == unique_chars[i] or c == unique_chars[j]]
            if all(filtered[k] != filtered[k + 1] for k in range(len(filtered) - 1)):
                max_len = max(max_len, len(filtered))
    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
