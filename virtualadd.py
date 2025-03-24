import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 5  # Initial number of people who receive the ad
    cumulative_likes = 0
    
    for day in range(1, n + 1):
        # Half of the people who receive the ad will like it
        liked = shared // 2
        
        # Add the likes for the current day to cumulative likes
        cumulative_likes += liked
        
        # Each person who liked the ad shares it with 3 friends for the next day
        shared = liked * 3
    
    return cumulative_likes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
