import numpy
numpy.set_printoptions(legacy='1.13')  # Ensure alignment of output matches the given format

# Read the dimensions
n, m = map(int, input().split())

# Create the identity-like array using numpy.eye
result = numpy.eye(n, m)

# Print the result
print(result)
