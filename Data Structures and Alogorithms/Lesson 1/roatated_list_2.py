from binarySearch import *

def search(arr: list[int],target: int):
    arr = sorted(arr)
    return binarysearch(arr,target)

arr = [1,5,6,0,0,1]

print(search(arr,3))