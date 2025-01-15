import numpy

# Read the input
input_list = list(map(int, input().split()))

# Convert the list into a 3x3 NumPy array
result = numpy.array(input_list).reshape(3, 3)

# Print the result
print(result)
