# Input the values of x and k
x, k = map(int, input().split())

# Input the polynomial as a string
polynomial = input()

# Evaluate the polynomial at x and check if it equals k
result = eval(polynomial) == k

# Print the result
print(result)
