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
def quickSort(nums, start=0, end=None):

    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quickSort(nums, start, pivot-1)
        quickSort(nums, pivot+1, end)

    return nums

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        nums = input()
        nums = list(map(int,nums.split()))
        quickSort(nums,0,len(nums)-1)
        S=0
        for i in range(len(nums)):
            S += nums[i] - nums[0]
        print(S)
        t-=1