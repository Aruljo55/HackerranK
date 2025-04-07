import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

from collections import Counter

def happyLadybugs(b):
    counts = Counter(b)
    
    if '_' not in b:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                continue
            return "NO"
        return "YES"
    else:
        for k, v in counts.items():
            if k != '_' and v == 1:
                return "NO"
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
