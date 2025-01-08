def print_formatted(number):
    # Calculate the width of the binary representation of the largest number
    width = len(bin(number)) - 2
    
    # Iterate through each number from 1 to the given number
    for i in range(1, number + 1):
        # Convert to decimal, octal, hexadecimal, and binary
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        # Print all values in the specified format
        print(f"{decimal} {octal} {hexadecimal} {binary}")
