import re
import email.utils

# Regex pattern based on rules
pattern = r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

n = int(input())
for _ in range(n):
    name_email = input()
    name, addr = email.utils.parseaddr(name_email)
    if re.match(pattern, addr):
        print(name_email)
