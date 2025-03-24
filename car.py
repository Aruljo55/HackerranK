import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
def circularArrayRotation(a, k, queries):
    n = len(a)
    
    # Optimize rotations by taking modulo, as n rotations brings the array back to original
    effective_rotations = k % n
    
    # Create a new array to store the result after rotations
    rotated = [0] * n
    
    # Perform the rotation by mapping each element to its new position
    for i in range(n):
        # Calculate the new position after rotation
        new_pos = (i + effective_rotations) % n
        rotated[new_pos] = a[i]
    
    # Return the values at the queried positions
    results = []
    for q in queries:
        results.append(rotated[q])
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
