from itertools import permutations

# Input string and size
s, k = input().split()
k = int(k)

# Generate permutations
result = permutations(sorted(s), k)

# Print each permutation on a separate line
for perm in result:
    print("".join(perm))
