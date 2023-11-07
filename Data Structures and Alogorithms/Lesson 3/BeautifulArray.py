def partition(nums,start=0,end=None):
    if end is None:
        end = len(nums) - 1
    l,r = start,end - 1
    while l<r:
        if nums[l] <= nums[start]:
            l+=1
        elif nums[r] > nums[start]:
            r-=1
        else:
            nums[r],nums[l] = nums[l],nums[r]
    if nums[r] < nums[start]:
        nums[r],nums[start] = nums[start],nums[r]
        return 1
    else:
        return start

def quickSort(nums,start=0,end=None):
    if end is None:
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)
    return nums

def check(nums):
    Sum = 0
    for i in range(len(nums)):
        j = i + 1
        Sum = Sum + nums[i] + nums[j]
        if Sum == nums[i+2]:
            return 0
    return 1
def sort(numbers):
    lenth = len(numbers)
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (numbers[i] < numbers[j]):
                # Hoán đổi vị trí
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
    return nums
if __name__ == '__main__':

    nums = list(map(int,input().split()))
    if check(nums) == 0:
        print('YES')
        nums = sort(nums)
        print(nums)
    else:
        print('NO')
    