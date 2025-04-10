import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
def almostSorted(arr):
    sorted_arr = sorted(arr)
    diff = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]

    if not diff:
        print("yes")
        return

    if len(diff) == 2:
        print("yes")
        print(f"swap {diff[0]+1} {diff[1]+1}")
        return

    # Check if reversing the subarray makes it sorted
    l, r = diff[0], diff[-1]
    if arr[l:r+1] == sorted_arr[l:r+1][::-1]:
        print("yes")
        print(f"reverse {l+1} {r+1}")
    else:
        print("no")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
