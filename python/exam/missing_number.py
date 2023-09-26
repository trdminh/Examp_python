def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 5, 10, 11, 12, 15, 16, 17, 19, 20]
print(findMissingNumbers(listOfNumbers))