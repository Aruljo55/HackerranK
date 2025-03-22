import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    # Calculate the maximum height of letters in the word
    max_height = 0
    for char in word:
        # Get the index of the current character in the alphabet (0-25)
        # by subtracting the ASCII value of 'a' from the ASCII value of the character
        char_index = ord(char) - ord('a')
        
        # Get the height of the current character from the heights array
        char_height = h[char_index]
        
        # Update the maximum height if the current character is taller
        if char_height > max_height:
            max_height = char_height
    
    # Calculate the area: width of the word (number of characters) x maximum height
    # Each character has a width of 1 unit
    area = len(word) * max_height
    
    return area
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
