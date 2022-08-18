# Given an array of integers, find the subarray with the maximum sum and return the maximum sum

def maxsumsubarray(nums):
    maxsum = nums[0]
    currsum = 0

    for n in nums:
        if currsum < 0:
            currsum = 0
        currsum += n
        maxsum = max(maxsum, currsum)
    return maxsum

print(maxsumsubarray([2,7,9,11,15]))


# handling negatives

def maxsubarraysum(nums):
    maxsum = nums[0]
    currsum = nums[0]
    for i in range(1, len(nums)):
        currsum = max(nums[i], currsum + nums[i])
        maxsum = max(maxsum, currsum)
    
    return maxsum