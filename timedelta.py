from datetime import datetime

# Input: number of test cases
t = int(input())

# Define the format of the input timestamps
timestamp_format = "%a %d %b %Y %H:%M:%S %z"

# Process each test case
for _ in range(t):
    # Read the two timestamps
    time1 = input().strip()
    time2 = input().strip()
    
    # Parse timestamps into datetime objects
    dt1 = datetime.strptime(time1, timestamp_format)
    dt2 = datetime.strptime(time2, timestamp_format)
    
    # Calculate the absolute difference in seconds
    difference = abs(int((dt1 - dt2).total_seconds()))
    
    # Output the difference
    print(difference)
