# Number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the first set A
    a_size = int(input())
    a = set(map(int, input().split()))
    
    # Read the second set B
    b_size = int(input())
    b = set(map(int, input().split()))
    
    # Check if set A is a subset of set B
    print(a.issubset(b))
