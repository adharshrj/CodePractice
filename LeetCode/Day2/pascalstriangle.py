# Given an input n representing the number lines, print pascals triangle of lines n.

def pascalstriangle(n):
    res = [[1]]
    for i in range(n-1):
        temp = [1]
        for j in range(len(res)-1):
            temp.append(res[i][j] + res[i][j+1])
        temp.append(1)
        res.append(temp)
    return res

print(pascalstriangle(8))