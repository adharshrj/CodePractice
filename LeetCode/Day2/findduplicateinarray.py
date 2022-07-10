# Find the duplicate number in the array
# Hint: Use floyd's cycle finding algorithm

def hasduplicate(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if fast == slow:
            break
    
    return slow