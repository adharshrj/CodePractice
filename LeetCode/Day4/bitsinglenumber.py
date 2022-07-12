# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def singlenumber(nums):
    res = 0
    for n in nums:
        res = res ^ n
    
    return res
