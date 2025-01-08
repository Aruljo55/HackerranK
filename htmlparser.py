from html.parser import HTMLParser

# Subclass HTMLParser
class MyHTMLParser(HTMLParser):
    
    # Handle start tag
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")
    
    # Handle end tag
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    # Handle start/end tag (empty tag)
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")

# Input reading
n = int(input())  # Number of lines in the HTML snippet
html_snippet = "\n".join(input() for _ in range(n))

# Create a parser instance and feed the HTML snippet
parser = MyHTMLParser()
parser.feed(html_snippet)
