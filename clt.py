def climbingLeaderboard(ranked, player):
    # Remove duplicates from ranked scores and maintain descending order
    unique_ranked = []
    for score in ranked:
        if not unique_ranked or score != unique_ranked[-1]:
            unique_ranked.append(score)
    
    # Initialize variables
    results = []
    i = len(unique_ranked) - 1  # Start from the lowest ranked score
    
    # Process each player's score
    for score in player:
        # Move up the leaderboard until we find the right position
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1
        
        # Calculate rank (i + 2 because i is 0-indexed and we add 1 more for the player's position)
        rank = i + 2
        results.append(rank)
    
    return results

# The problem expects each rank to be printed on a separate line, not as a list
if __name__ == '__main__':
    n = int(input().strip())
    ranked = list(map(int, input().strip().split()))
    m = int(input().strip())
    player = list(map(int, input().strip().split()))
    
    result = climbingLeaderboard(ranked, player)
    
    # Print each rank on a new line
    for rank in result:
        print(rank)