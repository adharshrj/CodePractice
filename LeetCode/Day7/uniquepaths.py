# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: m = 3, n = 7
# Output: 28

def uniquepath(m, n):
    res = [[1 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            res[i][j]=res[i-1][j] + res[i][j-1]
    
    return res[m-1][n-1]

