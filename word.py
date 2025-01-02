from collections import Counter, OrderedDict

# Custom Ordered Counter to maintain the order of first appearance
class OrderedCounter(Counter, OrderedDict):
    pass

# Input number of words
n = int(input().strip())

# Read the words into a list
words = [input().strip() for _ in range(n)]

# Create an OrderedCounter for word frequencies
word_counts = OrderedCounter(words)

# Output the number of distinct words
print(len(word_counts))

# Output the occurrences of each word in order of appearance
print(" ".join(map(str, word_counts.values())))
