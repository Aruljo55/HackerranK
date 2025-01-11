from itertools import product

# Input the two lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the Cartesian product of A and B
result = product(A, B)

# Print the output as space-separated tuples
print(" ".join(map(str, result)))
