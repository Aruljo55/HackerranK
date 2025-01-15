import numpy

# Read dimensions
n, m = map(int, input().split())

# Read the array
array = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Compute the sum along axis 0
sum_along_axis_0 = numpy.sum(array, axis=0)

# Compute the product of the sum
result = numpy.prod(sum_along_axis_0)

# Print the result
print(result)
