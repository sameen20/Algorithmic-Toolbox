# Uses python3
def calc_fib(n):
    arr = [0]*(n+2) #不能對空數組進行操作⋯⋯所以不能對空數組指定位置
    arr[0] = 0
    arr[1] = 1
    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]

n = int(input())
print(calc_fib(n))

"""
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
"""