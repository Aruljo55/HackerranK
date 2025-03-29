#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # Initial energy level is 100
    energy = 100
    
    # Current position (starting at cloud 0)
    position = 0
    
    # Jump until we return to cloud 0
    while True:
        # Calculate the next position using modulo to handle circular path
        position = (position + k) % len(c)
        
        # Lose 1 energy for the jump
        energy -= 1
        
        # If we land on a thundercloud (c[position] == 1), lose 2 more energy
        if c[position] == 1:
            energy -= 2
        
        # If we've completed the circuit (returned to cloud 0), break the loop
        if position == 0:
            break
    
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    
    c = list(map(int, input().rstrip().split()))
    
    result = jumpingOnClouds(c, k)
    
    fptr.write(str(result) + '\n')
    fptr.close()