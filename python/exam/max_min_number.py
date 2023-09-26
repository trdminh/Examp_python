def maxNumber(n):
    max = 0
    current = 1
    while current < len(n):
        if n[max] < n[current]:
            max = current
        current += 1
    return n[max]

def minNumber(n):
    min = 0
    current = 1
    while current < len(n):
        if n[min] > n[current]:
            min = current
        current += 1
    return n[min]

list = [0,1,2,4,6,3,19,2,4]

print(maxNumber(list))
print(minNumber(list))