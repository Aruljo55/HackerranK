def count_substring(string, substring):
    count = 0
    start = 0  # Start position for searching
    
    # Loop through the string to find all occurrences of the substring
    while start < len(string):
        # Find the index of the substring starting from 'start'
        pos = string.find(substring, start)
        
        if pos == -1:  # If no more occurrences are found
            break
        
        count += 1  # Increment count for each occurrence
        start = pos + 1  # Move the start position to the next index
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    