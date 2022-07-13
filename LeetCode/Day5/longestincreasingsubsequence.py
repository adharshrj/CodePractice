# Given an integer array nums, return the length of the longest strictly increasing subsequence.

def longest(nums):
    temp = [1] * len(nums)
    res = float('-inf')

    for curr in range(len(nums)):
        for prev in range(curr):
            if nums[prev] < nums[curr]:
                temp[curr] = max(temp[curr], 1 + temp[prev])
        
        res = max(res, temp[curr])
    return res

def longest(nums):
    res = [1] * len(nums)

    for curr in range(len(nums)):
        for prev in range(curr):
            if nums[prev] < nums[curr]:
                res[curr] = max(res[curr], 1 + res[prev])
    
    return max(res)