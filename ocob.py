import os

def organizingContainers(container):
    n = len(container)
    
    # Calculate the total number of balls in each container
    container_capacity = [sum(row) for row in container]
    
    # Calculate the total number of each type of ball across all containers
    ball_count = [sum(container[i][j] for i in range(n)) for j in range(n)]
    
    # If sorted lists match, swapping is possible
    return "Possible" if sorted(container_capacity) == sorted(ball_count) else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())

        container = [list(map(int, input().rstrip().split())) for _ in range(n)]

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
