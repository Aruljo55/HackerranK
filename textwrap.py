import textwrap
    def wrap(string, max_width):
    # Using list comprehension and string slicing
         return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])