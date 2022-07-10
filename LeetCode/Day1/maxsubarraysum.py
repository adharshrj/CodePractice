# Given an array of integers, find the subarray with the maximum sum and return the maximum sum

def maxsumsubarray(nums):
    maxsum = 0
    currsum = 0

    for n in nums:
        if currsum < 0:
            currsum = 0
        currsum += n
        maxsum = max(maxsum, currsum)
    return maxsum

print(maxsumsubarray([2,7,9,11,15]))