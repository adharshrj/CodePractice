# Given an array of numbers,  return the maximum product

# Hint: Use Kadane's algorithm

def maxproductsubarray(nums):
    maxproduct = float('-inf')
    mx = 1
    mn = 1

    for n in nums:
        mx, mn = max(n, mx*n, mn*n), min(n, mx*n, mn*n)
        maxproduct = max(maxproduct, mx, mn)
    
    return maxproduct

print(maxproductsubarray([2,7,9,11,15]))