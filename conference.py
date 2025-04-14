def maxPresentations(scheduleStart, scheduleEnd):
    # Combine start and end times into a list of tuples
    presentations = list(zip(scheduleStart, scheduleEnd))
    
    # Sort presentations by their end time
    presentations.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = 0

    # Iterate through the sorted presentations
    for start, end in presentations:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()
