import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
               "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
               "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        return f"{numbers[h]} o' clock"
    elif m == 15:
        return f"quarter past {numbers[h]}"
    elif m == 30:
        return f"half past {numbers[h]}"
    elif m == 45:
        return f"quarter to {numbers[h + 1]}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{numbers[m]} {minute_word} past {numbers[h]}"
    else:
        minute_word = "minute" if (60 - m) == 1 else "minutes"
        return f"{numbers[60 - m]} {minute_word} to {numbers[h + 1]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
