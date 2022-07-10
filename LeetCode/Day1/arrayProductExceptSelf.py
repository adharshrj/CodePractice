# Given an array of integers return an array containing the product of all other 
# integers except self for each integer nums[i]

# Iterate through the array from left to right and vice versa (prefix and suffix/postfix)

def arrayproductexceptself(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

print(arrayproductexceptself([2,6,7,3,9]))