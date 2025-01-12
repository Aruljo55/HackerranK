import numpy

# Read dimensions
n, m = map(int, input().split())

# Read the first array
array_a = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Read the second array
array_b = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Perform the operations and print the results
print(numpy.add(array_a, array_b))        # Addition
print(numpy.subtract(array_a, array_b))  # Subtraction
print(numpy.multiply(array_a, array_b))  # Multiplication
print(numpy.floor_divide(array_a, array_b))  # Integer Division
print(numpy.mod(array_a, array_b))       # Modulus
print(numpy.power(array_a, array_b))     # Power
