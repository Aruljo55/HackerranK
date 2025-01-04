# Input parsing
n, m = map(int, input().split())  # n: number of elements in the array, m: number of elements in each set
arr = list(map(int, input().split()))  # The array of integers
set_a = set(map(int, input().split()))  # The set A
set_b = set(map(int, input().split()))  # The set B

# Initialize happiness to 0
happiness = 0

# Calculate the total happiness
for num in arr:
    if num in set_a:
        happiness += 1
    elif num in set_b:
        happiness -= 1

# Output the result
print(happiness)
