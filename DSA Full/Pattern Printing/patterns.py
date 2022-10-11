"""
Print the pattern:
    *****
    *****
    *****
    *****
    *****
"""

def nxn(n):
    for _ in range(n):
        print("*" * n)

print(nxn(5))


"""
Print the pattern:
    *
    **
    ***
    ****
    *****
"""
def oneton(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print("*", end=" ")
        print()

print(oneton(5))

"""
Print the pattern:
    1
    12
    123
    1234
    12345
"""
def oneton2(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()    

print(oneton2(5))

"""
Print the pattern:
    1
    22
    333
    4444
    55555
"""

def oneton3(n):
    for i in range(1, n + 1):
        for _ in range(1, i + 1):
            print(_, end=" ")
        print()

print(oneton3(5))

def ntoone(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end= " ")
        print()

print(ntoone(5))

def triangle(n):
    for i in range(n):
        for j in range(n + i):
            if j < (n-i-1):
                print(" ", end="")
            else:
                print("*", end="")
        print()

print(triangle(30))

def sometriange(n):
    res = []
    for i in range(1, n+1):
        arr = []
        for j in range(1,i):
            arr.append(j)
        res.append(arr)

    print(res)

print(sometriange(6))

    
