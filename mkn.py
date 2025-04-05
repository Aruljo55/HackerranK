def kaprekarNumbers(p, q):
    kaprekars = []  # List to store Kaprekar numbers

    for num in range(p, q + 1):
        square = str(num ** 2)  # Convert square to string
        d = len(str(num))  # Length of original number

        # Split into right and left parts
        right = int(square[-d:]) if square[-d:] else 0
        left = int(square[:-d]) if square[:-d] else 0

        # Check if sum of left and right equals original number
        if left + right == num:
            kaprekars.append(str(num))

    if kaprekars:
        print(" ".join(kaprekars))
    else:
        print("INVALID RANGE")

# Input handling
if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
