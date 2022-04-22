# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    arr = [0]*(n+1)
    arr[0] = 0
    arr[1] = 1
    if n <= 1:
        return n % 10
    else:
        for i in range(2, n+1):
            arr[i] = (arr[i-1] + arr[i-2]) % 10
        return arr[n]


if __name__ == '__main__':
    input = sys.stdin.read() #input()的話，只能讀一個數字，在回車之後就沒了。在vscode裡面，回車之後按ctrl+d
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

"""   
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
"""