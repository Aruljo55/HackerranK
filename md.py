import sys

def minimumDistances(a):
    index_map = {}  # Store first occurrence of each number
    min_distance = float('inf')

    for i, num in enumerate(a):
        if num in index_map:
            min_distance = min(min_distance, i - index_map[num])
        index_map[num] = i  # Store latest index
    
    return min_distance if min_distance != float('inf') else -1

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))

    result = minimumDistances(a)

    print(result)  # Output result
