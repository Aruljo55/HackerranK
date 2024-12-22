n, m = map(int, input().split())  # Read n (number of rows) and m (number of attributes per row)
data = []

# Read the next n lines of data
for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)

k = int(input())  # Read the attribute index to sort by

# Sort the data based on the k-th attribute, maintaining the order for equal elements
sorted_data = sorted(data, key=lambda x: x[k])

# Print the sorted data
for row in sorted_data:
    print(" ".join(map(str, row)))
