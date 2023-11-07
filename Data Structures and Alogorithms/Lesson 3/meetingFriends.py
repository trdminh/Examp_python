def Sort(nums):
    for _ in range(len(nums) - 1):    
        for i in range(len(nums) - 1): 
            if nums[i] > nums[i+1]:  
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
    
            

if __name__ == '__main__':
    nums = input()
    nums = list(map(int,nums.split()))
    Sort(nums)
    S = nums[2] - nums[0]
    print(S)
        