from collections import Counter

# Input
s = input().strip()

# Count occurrences of each character
char_count = Counter(s)

# Sort characters: first by count (descending), then alphabetically (ascending)
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

# Output the top 3 most common characters
for char, count in sorted_chars[:3]:
    print(f"{char} {count}")
