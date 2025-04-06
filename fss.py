import math
import os
import random
import re
import sys
def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = 0

    for i in range(n):
        # Find the distance to the closest space station
        closest = min([abs(i - station) for station in c])
        max_distance = max(max_distance, closest)

    return max_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
