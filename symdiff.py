if __name__ == '__main__':
    m = int(input())  # Read size of set a
    a = set(map(int, input().split()))  # Read set a and convert to set of integers
    n = int(input())  # Read size of set b
    b = set(map(int, input().split()))  # Read set b and convert to set of integers

    # Find symmetric difference and sort the result
    result = sorted(a.symmetric_difference(b))

    # Print each element in the result on a new line
    for num in result:
        print(num)
