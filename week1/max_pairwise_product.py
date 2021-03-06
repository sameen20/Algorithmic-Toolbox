"""
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
"""

# Uses python3
def MaxPairwiseProduct(n,a,c):
    for i in range(0,n):
        for j in range (1,n):
            if a[i] != a[j]:
                m = a[i]*a[j]
                c.append(m)

            else:
                continue

    Product1 = max(c)
    return Product1

def MaxPairwiseProductFast(n,a):
    max_index1 = -1
    for i in range(0,n):
        if max_index1 == -1 or a[i] > a[max_index1]:
            max_index1 = i
        else:
            continue
    #the value of the other index should be different compared to the        
    #first, else it will assume the same indices for both the max
    """         
    max_index2 = -2
    for j in range(0,n):
        if a[j] > a[max_index2] and a[j] != a[max_index1]:
            max_index2 = j   
        else:
            continue
    """

    max_index2 = -1
    for j in range(0,n):
        if j != max_index1 and (max_index2 == -1 or a[j] > a[max_index2]):
            max_index2 = j
        else:
            continue


    Product2 = a[max_index1]*a[max_index2]
    return Product2

n = int(input())
a = [int(x) for x in input().split()]
c = list()

#print('The max value by regular algorithm:', MaxPairwiseProduct(n,a,c))
#print('The max value by faster algorithm:', MaxPairwiseProductFast(n,a))
print(MaxPairwiseProductFast(n,a))
