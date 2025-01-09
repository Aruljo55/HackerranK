if __name__ == '__main__':
    n = int(input())  # Read the number of elements in the tuple
    integer_list = tuple(map(int, input().split()))  # Create a tuple from space-separated integers
    print(hash(integer_list))  # Compute and print the hash of the tuple
