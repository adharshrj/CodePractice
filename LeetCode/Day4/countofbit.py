# Write a function that takes an unsigned integer and returns the number of '1' bits it has

def countofone(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    
    return count