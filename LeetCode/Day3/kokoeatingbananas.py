# Given an array of count of bananas, find the minimum hours in which koko can eat all bananas, 
# where h is the hour limit for all piles, len(piles) <= h

def kokoeatingbananas(piles, h):
    l, r = 1, len(piles)
    res = r

    while l <= r:
        m = (l+r)//2
        hours = 0
        for p in piles:
            hours += ((p-1)//m) + 1 #math.ceil(p/m)
        
        if hours <= h:
            res = min(res, m)
            r = m - 1
        
        else:
            l = m + 1
    
    return res