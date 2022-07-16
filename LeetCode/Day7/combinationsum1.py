# Given an array of numbers and a target return an array of combinations that add up to the target
# Repetetions allowed

# Use Backtracking

def combinationsum(nums, target):
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        
        if i >= len(nums) or total > target:
            return
        
        curr.append(nums[i])
        dfs(i, curr, total + nums[i])
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res


print(combinationsum([2,3,6,7], 7))