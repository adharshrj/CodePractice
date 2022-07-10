# Given a number num representing the number of stairs, calculate the number of ways in which you can climb those stairs.

def climbingstairs(num):
    a, b = 1, 1
    
    for i in range(1, num):
        res = a + b
        a = b
        b = res
    return b


import math;
def combination(n, r):
    return (int)(math.factorial(n)/(math.factorial(r) * math.factorial(n - r)))

def climbingstairsmath(num):
    res = 0
    r = 0
    while r <= num:
        res += combination(num, r)
        r += 1
        num -= 1

    return res
