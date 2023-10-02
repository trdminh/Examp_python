def searchInsertPosition(arr: list[int], target: int):
    l,r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

nums = [1,3,5,6]
target = 7

print(searchInsertPosition(nums,target))