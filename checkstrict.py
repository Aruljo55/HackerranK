# Reading the input
A = set(map(int, input().split()))  # The set A
n = int(input())  # Number of other sets

# Loop through each of the n sets and check the condition
for _ in range(n):
    B = set(map(int, input().split()))  # Read the current set B
    
    # Check if A is a strict superset of B
    if not (A.issuperset(B) and len(A) > len(B)):
        print(False)
        break
else:
    print(True)
