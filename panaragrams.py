import math
import os
import random
import re
import sys

def pangrams(s):
    return "pangram" if set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") else "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
