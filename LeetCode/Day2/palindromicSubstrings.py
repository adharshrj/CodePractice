#Given a string s return the number of palindromic substrings of the string
# Use helper function


def palinhelper(s, l, r):
    res = 0
    while l >= 0 and r<len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    
    return res

def palindromicsubstrings(s):
    res = 0
    for i in range(len(s)):
        res += palinhelper(s, i, i)
        res += palinhelper(s, i, i+1)
    
    return res