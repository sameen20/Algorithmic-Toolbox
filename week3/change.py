# Uses python3
import sys

def get_change(m):
    #write your code here
    amounts = 0
    if m < 5:
        return int(m/1)
    elif m>=5 and m < 10:
        left = m % 5
        if left == 0:
            amount = 1
        else:
            amount = 1 + left
        return int(amount)
    elif m >= 10:
        left = m % 10
        amount = m // 10
        if left < 5:
            amount += left
            return int(amount)
        elif left >= 5 and left < 10:
            left = left % 5
            if left == 0:
                amount += 1
            else:
                amount = 1 + left + amount
        return int(amount)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
