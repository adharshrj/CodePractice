# Given an array of numbers return the three numbers which add up to the target
# Sort the array if its not sorted

def threesum(nums, target):
    nums.sort()
    res = []

    for curr in range(len(nums)-2):
        if curr > 0 and nums[curr] == nums[curr-1]:
            continue
        if nums[curr] > 0:
            break

        nxt, last = curr + 1, len(nums)-1

        while nxt<last:
            tsum = nums[curr] + nums[nxt] + nums[last]
            if tsum == target:
                if len(res) == 0 or res[-1] != [nums[curr], nums[nxt], nums[last]]:
                    res.append([nums[curr], nums[nxt], nums[last]])
                nxt+=1
                last -=1
            elif tsum > target:
                last -=1
            else:
                nxt +=1

    return res

print(threesum([-1,0,1,2,-1,-4], 0))