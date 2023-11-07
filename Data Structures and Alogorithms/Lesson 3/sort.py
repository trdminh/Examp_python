from pandas import *
def normalSort(nums):
    nums = list(nums)
    for _ in range(len(nums) - 1):    
        for i in range(len(nums) - 1): 
            if nums[i] > nums[i+1]:  
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def insertionSort(nums):
    nums = list(nums)
    for i in range(len(nums) - 1):
        cur = nums.pop()
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1,cur)
    return nums

def selectionSort(nums):
    nums = list(nums)
    for i in range(len(nums)-1):
        min_index = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[min_index]:
                nums[j], nums[min_index] = nums[min_index], nums[j] 
    return nums

def merge(nums1, nums2):    
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):        
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums =  merge(left_sorted, right_sorted)
    return sorted_nums

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end-1
    while r > l:
       
        if nums[l] <= nums[end]:
            l += 1

        elif nums[r] > nums[end]:
            r -= 1
        
        
        else:
            nums[l], nums[r] = nums[r], nums[l]

    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
def quicksort(nums, start=0, end=None):

    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums
lst = [4,9,1,3,5,10,0]

lst = normalSort(lst)

print(lst)
