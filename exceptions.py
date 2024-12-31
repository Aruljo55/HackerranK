def handle_exceptions():
    # Reading the number of test cases
    t = int(input())

    for _ in range(t):
        try:
            # Reading the input values
            a, b = input().split()

            # Performing integer division and printing the result
            result = int(a) // int(b)
            print(result)

        except ZeroDivisionError as e:
            print("Error Code:", e)

        except ValueError as e:
            print("Error Code:", e)

# Example usage
handle_exceptions()