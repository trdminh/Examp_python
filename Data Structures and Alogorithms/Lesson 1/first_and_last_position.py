from binarySearch import *

        
        
def first_position(arr: list[int],target: int):
    index = binarysearch(arr,target)
    if index == False:
        return False
    else:
        while index >= 0 and arr[index] == target:
            if arr[index - 1] == target:
                index -= 1
            else:
                return index
    return index

def last_position(arr: list[int],target: int):
    index = binarysearch(arr,target)
    if index == False:
        return False
    else:
        while index >= 0 and arr[index] == target:
            if arr[index + 1] == target:
                index += 1
            else:
                return index
        return index
nums = [0,1,1,1,1,5,5,6,6,6,6,6,7]

target = 1

a = first_position(nums,target)
b = last_position(nums,target)
print(a)
print(b)