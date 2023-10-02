from binarySearch import *

def search2Dmatrix(matrix: list[list[int]],target: int):
    arr = []
    for i in matrix:
        arr += i
    return binarysearch(arr,target)

matrix = [[1,3,5,7],[11,13,15,17]]

print(search2Dmatrix(matrix,6))