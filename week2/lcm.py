# Uses python3
import sys
def lcm_naive(a, b):
    gcd = gcd_naive(a, b)
    return int((a*b)/gcd)

def gcd_naive(a, b):
    return gcd_naive(b, a%b) if b > 0 else a


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
"""
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
"""
