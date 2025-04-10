import math
import os
import random
import re
import sys

def get_all_pluses(grid, n, m):
    pluses = []

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 'G'

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'G':
                continue

            length = 0
            cells = {(i, j)}

            while True:
                length += 1
                new_cells = {
                    (i - length, j),
                    (i + length, j),
                    (i, j - length),
                    (i, j + length),
                }

                if all(is_valid(x, y) for x, y in new_cells):
                    cells.update(new_cells)
                    pluses.append((len(cells), set(cells)))  # (area, covered cells)
                else:
                    break

            # Also store the center-only plus (size 0 arms, area = 1)
            pluses.append((1, {(i, j)}))

    return pluses

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])

    pluses = get_all_pluses(grid, n, m)
    max_product = 0

    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            area1, cells1 = pluses[i]
            area2, cells2 = pluses[j]

            if cells1.isdisjoint(cells2):
                max_product = max(max_product, area1 * area2)

    return max_product


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
