# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    length = pisanoPeriod(m)

    arr = [0]*length
    arr[0] = 0
    arr[1] = 1
    for i in range(2, length):
        arr[i] = (arr[i-1] + arr[i-2]) % m

    remainder = n % length
    return arr[remainder]

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

"""
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
"""