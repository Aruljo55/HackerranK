from collections import OrderedDict

n = int(input())
ordered_items = OrderedDict()

for _ in range(n):
    *item_name, price = input().rsplit(maxsplit=1)
    item_name = " ".join(item_name)
    price = int(price)
    ordered_items[item_name] = ordered_items.get(item_name, 0) + price

for item, net_price in ordered_items.items():
    print(item, net_price)
