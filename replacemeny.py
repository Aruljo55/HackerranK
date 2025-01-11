from itertools import combinations_with_replacement

# Input string and size
s, k = input().split()
k = int(k)

# Generate and print combinations with replacement
for comb in combinations_with_replacement(sorted(s), k):
    print("".join(comb))
