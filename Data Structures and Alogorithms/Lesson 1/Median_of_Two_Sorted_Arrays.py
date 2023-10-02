def medianOfsortedArray(arr1: list[int],arr2: list[int]) -> float:
    arr = arr1 + arr2
    arr = sorted(arr)
    mid = (0+len(arr))//2
    if len(arr)%2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid])/2
    
nums1 = [1,2]
nums2 = [3,4]

print(medianOfsortedArray(nums1,nums2))