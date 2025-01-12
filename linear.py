import numpy as np

# Read the input
n = int(input())  # Dimension of the matrix
matrix = []

# Read each row and append to matrix
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert the matrix into a NumPy array
matrix = np.array(matrix)

# Compute the determinant using numpy.linalg.det
determinant = np.linalg.det(matrix)

# Print the determinant rounded to 2 decimal places
print(round(determinant, 2))
