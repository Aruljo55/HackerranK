from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total_combinations = list(combinations(range(n), k))
favorable_combinations = [1 for comb in total_combinations if any(letters[i] == 'a' for i in comb)]

probability = len(favorable_combinations) / len(total_combinations)
print(f"{probability:.4f}")
