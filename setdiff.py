n_english = int(input())
english_subscribers = set(map(int, input().split()))
n_french = int(input())
french_subscribers = set(map(int, input().split()))

only_english = english_subscribers.difference(french_subscribers)
print(len(only_english))
