class EvenStream:
    def __init__(self):
        self.current = 0  # Start with the first even number (0)

    def get_next(self):
        next_value = self.current
        self.current += 2  # Increment by 2 to get the next even number
        return next_value

class OddStream:
    def __init__(self):
        self.current = 1  # Start with the first odd number (1)

    def get_next(self):
        next_value = self.current
        self.current += 2  # Increment by 2 to get the next odd number
        return next_value

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()  # Default to EvenStream if no stream is provided
    for _ in range(n):
        print(stream.get_next())

# Sample Input
queries = [
    ('odd', 2),
    ('even', 3),
    ('odd', 5)
]

# Process each query
for stream_name, n in queries:
    if stream_name == 'odd':
        print_from_stream(n, OddStream())  # Use OddStream for 'odd' queries
    elif stream_name == 'even':
        print_from_stream(n)  # Default stream is EvenStream
