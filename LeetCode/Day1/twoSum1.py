# Given an unsorted array, check if the target is the sum of two numbers in the array, return the positions
# use hashmap

def twosum1(nums, target):
    oldmap = {}
    for i, n in enumerate(nums):
        diff = target - nums[i]
        if diff in oldmap:
            return [oldmap[diff], i]
        oldmap[n] = i
    return


print(twosum1([2,4,7,11,17], 24))