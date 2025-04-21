import re  # Import the regular expression module

# Function to validate the email
def fun(s):
    # Regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,10}$'
    
    # Return True if the email matches the pattern, otherwise False
    return bool(re.match(pattern, s))
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)