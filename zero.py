import numpy

# Read the shape of the array
shape = tuple(map(int, input().split()))

# Create and print the array filled with zeros
print(numpy.zeros(shape, dtype=numpy.int))

# Create and print the array filled with ones
print(numpy.ones(shape, dtype=numpy.int))
