from itertools import product

def maximize_modulo(K, M, lists):
    # Generate the Cartesian product of all lists
    cartesian_product = product(*lists)
    
    # Calculate the maximum value of the equation
    max_value = 0
    for combination in cartesian_product:
        value = sum(x**2 for x in combination) % M
        max_value = max(max_value, value)
    
    return max_value

if __name__ == "__main__":
    # Input handling
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        lst = list(map(int, input().split()))[1:]  # Ignore the first number in each line
        lists.append(lst)

    # Calculate and print the result
    result = maximize_modulo(K, M, lists)
    print(result)
