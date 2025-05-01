import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # Count attributes of the current node
    count = len(node.attrib)
    
    # Recursively count attributes in all child elements
    for child in node:
        count += get_attr_number(child)
    
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))