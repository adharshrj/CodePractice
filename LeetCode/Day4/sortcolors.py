# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Ex: Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]


def sortcolors(nums):
    l, m, h = 0, 0, len(nums)-1

    while m<=h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l+=1
            m+=1
        elif nums[m] == 1:
            m+=1
        elif nums[m] == 2:
            nums[m], nums[h] = nums[h], nums[m]
            h-=1
    return nums
        
