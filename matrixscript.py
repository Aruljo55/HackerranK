import re

# Input the number of rows and columns
rows, cols = map(int, input().split())

# Input the rows of the matrix script
matrix = [input() for _ in range(rows)]

# Initialize an empty list to store the decoded message
decoded_message = []

# Traverse through the matrix column by column
for c in range(cols):
    for r in range(rows):
        decoded_message.append(matrix[r][c])

# Join the decoded characters into a single string
decoded_script = ''.join(decoded_message)

# Replace non-alphanumeric characters between alphanumeric characters with a space
decoded_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)

# Print the final decoded message
print(decoded_script)
