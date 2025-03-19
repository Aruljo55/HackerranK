#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Special case for the transition year 1918
    if year == 1918:
        # In 1918, February 14th was the 32nd day of the year
        # So we have 31 (Jan) + 14 (Feb) - 13 days = 32 days for first 2 months
        # For the first 8 months: 31+14+31+30+31+30+31+31 = 229 days
        # 256 - 229 = 27, so the 256th day is the 27th of September
        return "26.09.1918"
    
    # Check if it's a leap year
    if year < 1918:  # Julian calendar
        leap_year = year % 4 == 0
    else:  # Gregorian calendar
        leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    # Calculate the day in September
    if leap_year:
        # In a leap year, first 8 months have 31+29+31+30+31+30+31+31 = 244 days
        # 256 - 244 = 12, so the 256th day is the 12th of September
        return f"12.09.{year}"
    else:
        # In a non-leap year, first 8 months have 31+28+31+30+31+30+31+31 = 243 days
        # 256 - 243 = 13, so the 256th day is the 13th of September
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()