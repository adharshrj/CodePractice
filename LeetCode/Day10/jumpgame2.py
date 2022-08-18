# Minumum number of jumps to end.

def jumpgame(nums):
    res = l = r = 0
    while r < len(nums) - 1:
        maxj = 0
        for i in range(l, r + 1):
            maxj = max(maxj, i + nums[i])
        l = r + 1
        r = maxj
        res += 1
    
    return res

print(jumpgame([2,3,0,1,4]))