# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threesumclosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]

    for curr in range(len(nums)-2):
        s1 = nums[curr] + nums[-2] + nums[-1]
        if s1 < target:
            if abs(s1 - target) < abs(res - target):
                res = s1
            continue
            
        s2 = nums[curr] + nums[curr + 1] + nums[curr + 2]
        if s2 > target:
            if abs(s2 - target) < abs(res - target):
                res = s2
            break

        nxt, lst = curr + 1, len(nums) - 1
        while nxt < lst:
            csum = nums[curr] + nums[nxt] + nums[lst]

            if csum == target:
                return csum
            
            if abs(csum - target) < abs(res - target):
                res = csum
            
            if csum < target:
                nxt += 1
            
            elif csum > target:
                lst -= 1
        
    return res