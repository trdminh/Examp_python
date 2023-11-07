def partition(nums,start=0,end=None):
    if end is None:
        end = len(nums) - 1
    l,r=start,end-1
    while r > l:
        if nums[l] <= nums[end]:
            l+=1
        elif nums[r] > nums[end]:
            r-=1
        else:
            nums[r],nums[l] = nums[l],nums[r]
    if nums[l] > nums[end]:
        nums[l],nums[end] = nums[end],nums[l]
        return 1
    else:
        return end
    
def quickSort(nums,start=0,end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)
    return nums

if __name__ == '__main__':
    n = int(input())
    A = input()
    A = list(map(int,A.split()))
    m = int(input())
    B = input()
    B = list(map(int,B.split()))
    quickSort(A,0,len(A)-1)
    quickSort(B,0,len(B)-1)
    print(A[n-1], B[m-1])
            
    