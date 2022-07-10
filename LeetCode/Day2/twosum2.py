# Given a sorted array, return the two numbers which add up to the target

def twosum2(nums, target):
    l = 0
    r = len(nums)-1
    while l < r:
        twosum = nums[l] + nums[r]
        if target == twosum:
            return [l+1, r+1] , [nums[l], nums[r]]
        elif target < twosum:
            r -= 1
        else:
            l+=1

print(twosum2([2,7,9,11,15], 24))