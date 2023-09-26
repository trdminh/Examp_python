import random
n = random.randrange(1,10)
value = int(input("Enter your choice:\n"))
while n != value:
    if n < value:
        print("Too high")
        value = int(input("Enter your choice:\n"))
    elif n > value:
        print("Too low")
        value = int(input("Enter your choice:\n"))
    else:
        break
print("That's correct")