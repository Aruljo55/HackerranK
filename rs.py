import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    """
    Calculate the number of occurrences of 'a' in the first n characters
    of an infinitely repeated string.
    
    Parameters:
    s (str): the string to repeat
    n (int): the number of characters to consider
    
    Returns:
    int: the frequency of 'a' in the first n characters
    """
    # Count occurrences of 'a' in the original string
    count_a_in_string = s.count('a')
    
    # Calculate how many complete copies of the string we need
    complete_copies = n // len(s)
    
    # Calculate how many characters from the partial copy we need
    remaining_chars = n % len(s)
    
    # Calculate total occurrences of 'a'
    total_count = (count_a_in_string * complete_copies) + s[:remaining_chars].count('a')
    
    return total_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
