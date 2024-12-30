def mutate_string(string, position, character):
    # Convert the string to a list
    string_list = list(string)
    
    # Modify the character at the given position
    string_list[position] = character
    
    # Join the list back into a string and return it
    return ''.join(string_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)