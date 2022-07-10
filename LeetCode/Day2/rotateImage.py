# Given an image in the form of a matrix rotate the image by 90* and return the output.

def rotateimage(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(0, rows):
        for j in range(i, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(0, rows):
        for j in range(0, rows//2):
            matrix[i][j], matrix[i][rows-1-j] = matrix[i][rows-1-j], matrix[i][j]