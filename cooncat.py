import numpy

# Read the dimensions of the arrays
n, m, p = map(int, input().split())

# Read the first array
array_1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    array_1.append(row)

# Read the second array
array_2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    array_2.append(row)

# Convert both arrays to NumPy arrays
array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)

# Concatenate the arrays along axis 0
result = numpy.concatenate((array_1, array_2), axis=0)

# Print the result
print(result)
