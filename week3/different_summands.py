# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    if n <= 2:
        summands.append(n)
    else:
        while n > 0:
            if n - i > i:
                summands.append(i)
            else:
                summands.append(n)
                break
            n -= i
            i += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
