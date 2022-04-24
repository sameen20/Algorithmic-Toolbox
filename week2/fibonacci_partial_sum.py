# Uses python3
import sys
def fibonacci_partial_sum_naive(from_, to):
    from_ %= 60
    to %= 60
    if from_ <= to:
        n = to
    else: 
        n = from_
    f = [0]*(n+3)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+3):
        f[i] = f[i-1] + f[i-2]
    return ((f[to+2]-1) - (f[from_+1]-1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
"""
def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
"""