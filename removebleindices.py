#!/bin/python3

import sys

def getRemovableIndices(str1, str2):
    removable = []
    
    for i in range(len(str1)):
        modified_str = str1[:i] + str1[i+1:]
        if modified_str == str2:
            removable.append(i)
    
    return removable if removable else [-1]

if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    result = getRemovableIndices(str1, str2)
    print('\n'.join(map(str, result)))
