s = input()
print(''.join(sorted(s, key=lambda x: (x.isdigit() - x.islower(), x.isdigit() and int(x) % 2 == 0, x))))
