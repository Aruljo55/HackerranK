class EvenStream:
    def __init__(self):
        self.current = 0
    
    def get_next(self):
        result = self.current
        self.current += 2
        return result

class OddStream:
    def __init__(self):
        self.current = 1
    
    def get_next(self):
        result = self.current
        self.current += 2
        return result

def print_from_stream(n, stream=None):
    # If stream is not provided, default to EvenStream
    if stream is None:
        stream = EvenStream()
    
    for _ in range(n):
        print(stream.get_next())
