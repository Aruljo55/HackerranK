def score_words(words):
    vowels = "aeiouy"
    score = 0
    
    for word in words:
        # Count the vowels in the current word
        num_vowels = sum(1 for letter in word if letter in vowels)
        # Add 2 if the number of vowels is even, otherwise add 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    
    return score

if __name__ == "__main__":
    n = int(input())
    words = input().split()
    print(score_words(words))
