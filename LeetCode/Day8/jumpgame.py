# Given an array of numbers n, check whether we can reach the end by moving <n spaces in each turn.

# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

def jumpgame(nums):
    goal = len(nums) - 1

    for i in range(len(nums) -1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return True if goal == 0 else False