#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Initialize result to 1
    factorial = 1
    
    # Multiply from 2 to n
    for i in range(2, n + 1):
        factorial *= i
    
    # Print the factorial
    print(factorial)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)