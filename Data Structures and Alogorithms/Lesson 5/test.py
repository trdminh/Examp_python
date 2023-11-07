import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

## s = "A man, a plan, a canal: Panama"

## s = remove_punctuation(s.lower())
## s = "".join(s.split())


## print(s)
##nums = [4,2,1,2,1]
##l = list(set(nums))

##print(l)
'''
from math import *
def check( n: int) -> list[list[int]]:
    c = []
    for i in range(1,n+1):
        if n % i == 0:
            c.append([i,int(n/i)])
    return c
t = check(4)
mid = len(t)//2
print(t[mid])

'''

c = 1
print(int(6**0.5))