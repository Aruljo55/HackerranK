import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Calculate how many squares the queen can attack on the chessboard
    
    Parameters:
    n (int): size of the chessboard (n x n)
    k (int): number of obstacles
    r_q (int): row position of the queen
    c_q (int): column position of the queen
    obstacles (list): positions of obstacles as [row, column] pairs
    
    Returns:
    int: number of squares the queen can attack
    """
    # Convert obstacles to a set for O(1) lookup
    obstacle_set = {(ob[0], ob[1]) for ob in obstacles}
    
    # Define the 8 directions: horizontal, vertical, diagonals
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Up
        (-1, 0),  # Down
        (1, 1),   # Up-Right
        (1, -1),  # Up-Left
        (-1, 1),  # Down-Right
        (-1, -1)  # Down-Left
    ]
    
    total_squares = 0
    
    # Check each direction
    for dr, dc in directions:
        r, c = r_q, c_q
        
        # Move in current direction until hitting obstacle or board edge
        while True:
            r += dr
            c += dc
            
            # Check if we're still on the board
            if r < 1 or r > n or c < 1 or c > n:
                break
                
            # Check if there's an obstacle at this position
            if (r, c) in obstacle_set:
                break
                
            # Valid square the queen can attack
            total_squares += 1
    
    return total_squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
