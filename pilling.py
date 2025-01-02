def can_stack_cubes(n, blocks):
    left, right = 0, n - 1
    last = float('inf')  # The last cube stacked, initially set to infinity (large value)

    while left <= right:
        # Select the larger of the two boundary cubes that is <= `last`
        if blocks[left] >= blocks[right]:
            if blocks[left] <= last:
                last = blocks[left]
                left += 1
            else:
                return "No"
        else:
            if blocks[right] <= last:
                last = blocks[right]
                right -= 1
            else:
                return "No"
    
    return "Yes"

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n = int(input())  # Number of cubes
    blocks = list(map(int, input().split()))  # List of cubes' side lengths

    # Output result for each test case
    print(can_stack_cubes(n, blocks))
