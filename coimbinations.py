from itertools import combinations

# Input string and size
s, k = input().split()
k = int(k)

# Generate and print combinations
for i in range(1, k + 1):
    for comb in combinations(sorted(s), i):
        print("".join(comb))
