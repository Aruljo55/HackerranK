from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")
    
    def handle_endtag(self, tag):
        # End tags are not needed for this task, so we ignore them
        pass
    
    def handle_comment(self, data):
        # Ignore content inside comments
        pass

# Input reading
n = int(input())  # Number of lines in the HTML snippet
html_snippet = "\n".join(input() for _ in range(n))

# Create a parser instance and feed the HTML snippet
parser = MyHTMLParser()
parser.feed(html_snippet)
