# Given an array of heights, calculate the area of the largest container that can be made using two heights.

def containerwithmostwater(heights):
    l, r = 0, len(heights) - 1
    maxarea = 0

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        maxarea = max(area, maxarea)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    
    return maxarea
    
print(containerwithmostwater([1,8,6,2,5,4,8,3,7]))