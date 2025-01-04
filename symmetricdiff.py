n_english = int(input())
english_subscribers = set(map(int, input().split()))
n_french = int(input())
french_subscribers = set(map(int, input().split()))

exclusive_subscribers = english_subscribers.symmetric_difference(french_subscribers)
print(len(exclusive_subscribers))
