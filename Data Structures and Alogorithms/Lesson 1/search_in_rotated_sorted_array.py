def search(arr: list[int], target: int):
        n = len(arr) 
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == target:
                return mid
            elif arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[right] >= arr[mid]:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        