import os

def biggerIsGreater(w):
    # Convert string to a list (because strings are immutable in Python)
    w = list(w)
    
    # Step 1: Find pivot (rightmost char smaller than next char)
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    
    if i == -1:
        return "no answer"  # Already the largest permutation
    
    # Step 2: Find the smallest character to the right of pivot that is larger than pivot
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    
    # Step 3: Swap pivot and successor
    w[i], w[j] = w[j], w[i]
    
    # Step 4: Reverse the suffix to get the next smallest lexicographic order
    w = w[:i + 1] + w[i + 1:][::-1]
    
    return "".join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for _ in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')

    fptr.close()
