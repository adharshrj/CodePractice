# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
#   Integers in each row are sorted from left to right.
#   The first integer of each row is greater than the last integer of the previous row.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


def search(matrix, target):
    l, r = 0, len(matrix) - 1
    t,b = 0, len(matrix[0]) - 1

    while l<=r:
        mid = (l+r)//2

        if matrix[mid][0] > target:
            r = mid - 1
        elif matrix[mid][-1] < target:
            l = mid + 1
        else:
            break
    
    mid = (l+r)//2
    while t<=b:
        m = (t + b)//2
        if matrix[mid][m] > target:
            b = m - 1
        elif matrix[mid][m] < target:
            t = m + 1
        else:
            return True
    return False

