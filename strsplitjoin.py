def split_and_join(line):
    # Split the string on spaces and then join the list with a hyphen
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)