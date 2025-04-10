import math
import os
import random
import re
import sys

def bomberMan(n, grid):
    if n == 1:
        return grid

    def detonate(current_grid):
        rows = len(current_grid)
        cols = len(current_grid[0])
        result = [['O'] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if current_grid[i][j] == 'O':
                    result[i][j] = '.'
                    if i > 0:
                        result[i-1][j] = '.'
                    if i < rows - 1:
                        result[i+1][j] = '.'
                    if j > 0:
                        result[i][j-1] = '.'
                    if j < cols - 1:
                        result[i][j+1] = '.'
        return [''.join(row) for row in result]

    # First explosion after full bomb grid
    first = detonate(grid)
    # Second explosion pattern
    second = detonate(first)

    if n % 2 == 0:
        return ['O' * len(grid[0]) for _ in range(len(grid))]
    elif n % 4 == 3:
        return first
    elif n % 4 == 1:
        return second

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
