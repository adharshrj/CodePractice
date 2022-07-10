# For a zero in the matrix, set the top, bottom, left and right elements as Zeros.

def setmatrixzeros(matrix):
    rows, cols, temp = len(matrix), len(matrix[0]), 1
    for i in range(0, rows):
        if matrix[i][0] == 0:
            temp = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(rows-1,-1,-1):
        for j in range(cols-1,0,-1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0 
        if temp == 0:
            matrix[i][0] = 0

print(setmatrixzeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))