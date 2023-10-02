def count_rotations(arr: list[int]):
    n = len(arr) 
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right)//2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        elif arr[mid] >= arr[left]:
            left = mid + 1
    return 0


nums = [3, 2, 4, 1] 

a = count_rotations(nums)
print(a)