n_english = int(input())
english_subscribers = set(map(int, input().split()))
n_french = int(input())
french_subscribers = set(map(int, input().split()))

common_subscribers = english_subscribers.intersection(french_subscribers)
print(len(common_subscribers))
