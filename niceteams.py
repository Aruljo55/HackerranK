def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    left, right, count = 0, 1, 0
    n = len(skillLevel)
   
    while right < n:
        if skillLevel[right] - skillLevel[left] >= minDiff:
            count += 1
            left += 1  # Move both pointers to avoid reusing players
        right += 1  # Move right pointer to find a new valid pair

        if left >= right:  # Ensure left pointer is always behind right
            right = left + 1
   
    return count