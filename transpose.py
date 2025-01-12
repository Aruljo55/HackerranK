import numpy

# Read the dimensions of the matrix
n, m = map(int, input().split())

# Read the matrix data
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert the list to a NumPy array
my_array = numpy.array(matrix)

# Print the transpose
print(numpy.transpose(my_array))

# Print the flattened array
print(my_array.flatten())
