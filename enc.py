import os
import math

def encryption(s):
    # Remove spaces
    s = s.replace(" ", "")
    L = len(s)

    # Find grid dimensions
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))

    # Ensure the grid can fit all characters
    if rows * cols < L:
        rows += 1

    # Encrypt the message by reading column-wise
    encrypted_words = []
    for col in range(cols):
        encrypted_word = "".join(s[i] for i in range(col, L, cols))
        encrypted_words.append(encrypted_word)
    
    return " ".join(encrypted_words)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')  # Use default file for testing

    s = input().strip()

    result = encryption(s)

    fptr.write(result + '\n')
    fptr.close()
