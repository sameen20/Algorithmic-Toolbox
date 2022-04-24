# Uses python3
from sys import stdin
def fibonacci_sum_squares_naive(n):
    n %= 60
    f = [0]*(n+2)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+2):
        f[i] = f[i-1] + f[i-2]
    return (f[n] * f[n+1]) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
"""
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
"""