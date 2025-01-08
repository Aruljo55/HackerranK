from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    
    def handle_data(self, data):
        if data.strip():  # Exclude newlines or whitespace-only data
            print(">>> Data")
            print(data)

# Input reading
n = int(input())  # Number of lines in the HTML snippet
html_snippet = "\n".join(input() for _ in range(n))

# Create a parser instance and feed the HTML snippet
parser = MyHTMLParser()
parser.feed(html_snippet)
