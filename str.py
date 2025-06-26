import math
import os
import random
import re
import sys

def hackerrankInString(s):
    target = "hackerrank"
    idx = 0
    for char in s:
        if idx < len(target) and char == target[idx]:
            idx += 1
    return "YES" if idx == len(target) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
