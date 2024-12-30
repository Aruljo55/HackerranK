def print_formatted(number):
    # Determine the width for formatting based on the binary representation of 'number'
    width = len(bin(number)) - 2  # Length of binary representation without '0b'
    
    # Loop through numbers from 1 to the given number
    for i in range(1, number + 1):
        # Print each number in decimal, octal, hexadecimal (uppercase), and binary
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

# Read input from stdin (For environments where the input is provided automatically)
if __name__ == "__main__":
    n = int(input())  # The input value for n
    print_formatted(n)
