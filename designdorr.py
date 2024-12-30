def design_mat(n, m):
    # Calculate the number of rows above and below "WELCOME"
    pattern_rows = (n - 1) // 2
    
    # Generate the upper part of the mat
    for i in range(1, pattern_rows + 1):
        # Form the pattern with increasing number of .|. symbols
        pattern = (".|." * (2 * i - 1)).center(m, '-')
        print(pattern)
    
    # Middle "WELCOME" row
    welcome_row = "WELCOME".center(m, '-')
    print(welcome_row)
    
    # Generate the lower part of the mat (mirroring the upper part)
    for i in range(pattern_rows, 0, -1):
        pattern = (".|." * (2 * i - 1)).center(m, '-')
        print(pattern)

# Sample input
n, m = 7, 21
design_mat(n, m)
