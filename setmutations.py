# Reading the initial set and number of operations
n = int(input())  # number of elements in the set
A = set(map(int, input().split()))  # the initial set A

# Reading the number of other sets (operations)
m = int(input())

# Performing the operations
for _ in range(m):
    # Read the operation and the size of the other set
    operation, _ = input().split()
    
    # Read the elements of the other set
    other_set = set(map(int, input().split()))
    
    # Perform the respective mutation operation
    if operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "update":
        A.update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)

# After all operations, print the sum of elements in set A
print(sum(A))
