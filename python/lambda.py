def squared(num) : return num*num

numbers = [2,5,6,4,12]

squared_num = map(lambda num : num*num, numbers)

print(list(squared_num))

from functools import reduce

lambda acc, curr : acc + curr

total = reduce(lambda acc, curr : acc + curr,numbers)

print(total)