import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0])
    layers = []

    # Step 1: Extract layers
    num_layers = min(m, n) // 2
    for layer in range(num_layers):
        elements = []
        # Top
        for i in range(layer, n - layer):
            elements.append(matrix[layer][i])
        # Right
        for i in range(layer + 1, m - 1 - layer):
            elements.append(matrix[i][n - 1 - layer])
        # Bottom
        for i in range(n - 1 - layer, layer - 1, -1):
            elements.append(matrix[m - 1 - layer][i])
        # Left
        for i in range(m - 2 - layer, layer, -1):
            elements.append(matrix[i][layer])
        layers.append(elements)

    # Step 2: Rotate each layer
    for i in range(len(layers)):
        rot = r % len(layers[i])
        layers[i] = layers[i][rot:] + layers[i][:rot]

    # Step 3: Write layers back
    for layer in range(num_layers):
        idx = 0
        # Top
        for i in range(layer, n - layer):
            matrix[layer][i] = layers[layer][idx]
            idx += 1
        # Right
        for i in range(layer + 1, m - 1 - layer):
            matrix[i][n - 1 - layer] = layers[layer][idx]
            idx += 1
        # Bottom
        for i in range(n - 1 - layer, layer - 1, -1):
            matrix[m - 1 - layer][i] = layers[layer][idx]
            idx += 1
        # Left
        for i in range(m - 2 - layer, layer, -1):
            matrix[i][layer] = layers[layer][idx]
            idx += 1

    # Step 4: Print result
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
