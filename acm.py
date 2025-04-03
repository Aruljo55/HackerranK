import os

def acmTeam(topic):
    max_topics = 0
    team_count = 0
    n = len(topic)
    
    for i in range(n):
        for j in range(i + 1, n):  # Ensure unique pairs
            combined_knowledge = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            
            if combined_knowledge > max_topics:
                max_topics = combined_knowledge
                team_count = 1
            elif combined_knowledge == max_topics:
                team_count += 1

    return [max_topics, team_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = [input().strip() for _ in range(n)]

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)) + '\n')
    fptr.close()
