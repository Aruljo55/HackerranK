import numpy

# Set print options to match the required output format
numpy.set_printoptions(sign=' ')

# Read input
A = numpy.array(list(map(float, input().split())))

# Print the floor, ceil, and rint
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
