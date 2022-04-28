#Uses python3

import sys, functools

def largest_number(a):
    #write your code here
    a = sorted(a, key=functools.cmp_to_key(compare))
    return str(int("".join(a)))

def compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
