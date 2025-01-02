from collections import deque

# Input number of operations
n = int(input().strip())

# Initialize an empty deque
d = deque()

# Perform the operations
for _ in range(n):
    operation = input().strip().split()
    method = operation[0]
    if len(operation) > 1:  # If there's a value with the method
        getattr(d, method)(operation[1])
    else:  # For methods without additional arguments like pop or popleft
        getattr(d, method)()

# Output the space-separated elements of the deque
print(" ".join(d))
