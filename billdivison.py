#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Remove the item Anna didn't eat
    anna_bill = bill.copy()
    anna_bill.pop(k)
    
    # Calculate Anna's actual share
    actual_share = sum(anna_bill) // 2
    
    # Check if Brian charged the correct amount
    if b == actual_share:
        print("Bon Appetit")
    else:
        # Brian overcharged, calculate the refund
        refund = b - actual_share
        print(refund)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)