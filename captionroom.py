from collections import Counter

def find_captain_room(k, room_list):
    # Count the frequency of each room number
    room_count = Counter(room_list)
    
    # Iterate over the room counts and find the room number that appears exactly once
    for room, count in room_count.items():
        if count == 1:
            return room

# Input Reading
k = int(input())  # The size of each group
room_list = list(map(int, input().split()))  # The list of room numbers

# Finding and printing the Captain's room number
print(find_captain_room(k, room_list))
