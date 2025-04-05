import sys

def beautifulTriplets(d, arr):
    count = 0
    values = set(arr)  # Use a set for fast lookups
    
    for num in arr:
        if num + d in values and num + 2 * d in values:
            count += 1
    
    return count

# Input handling
if __name__ == '__main__':
    # Read input correctly for HackerRank
    n, d = map(int, sys.stdin.readline().split())  # Read first line
    arr = list(map(int, sys.stdin.readline().split()))  # Read array
    
    # Compute result
    result = beautifulTriplets(d, arr)
    
    # Print the result (or use sys.stdout.write if needed)
    print(result)
