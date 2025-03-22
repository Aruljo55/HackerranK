import os
import random
import re
import sys

def angryProfessor(k, a):
    # Count the number of students who arrived on time or early
    on_time_count = 0
    for arrival_time in a:
        if arrival_time <= 0:
            on_time_count += 1
    
    # If the number of on-time students is less than the threshold,
    # the class is cancelled
    if on_time_count < k:
        return "YES"
    else:
        return "NO"  
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
