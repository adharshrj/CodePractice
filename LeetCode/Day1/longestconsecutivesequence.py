# Given a string of characters return the longest consecutive sequence without repeating characters

# Use set(input) then calculate length, return the longest length

def longestconsecutivesequence(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if n-1 not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    
    return longest

print(longestconsecutivesequence([100,1,200,2,3,400,4,21,5]))
