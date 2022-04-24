# Uses python3
#from fcntl import F_GETLK64
import sys

def get_fibonacci_last_digit(n):
    n %= 60
    if n <= 1:
        return n
    else:
        f = [0]*(n+1)
        f[0] = 0
        f[1] = 1
        res = 1
        for i in range(2, n+1):
            f[i] = (f[i-1] + f[i-2]) % 10
            res += f[i]
        return res % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
    
"""
def fibonacci_sum_naive(n):
    pre = 0
    curr = 1
    n = n % 60
    if n <= 1:
        return n
    else:
        for i in range(2, n+2):
            pre, curr = curr, (pre+curr)

        return (pre+curr)%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
-------

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
"""