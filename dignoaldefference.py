import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    leftdiag = rightdiag=0
    for i in range(n):
        leftdiag+=arr[i][i]
        rightdiag+=arr[i][n-1-i]
    return abs(leftdiag-rightdiag)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
