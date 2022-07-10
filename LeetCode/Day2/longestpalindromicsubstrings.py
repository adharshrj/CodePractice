#Given a string return the longest palindromic substring of the string


def palinhelper(s, l, r):
    while l >= 0 and r<len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1: r]
        

def longestpalindrome(s):
    res = ""
    for i in range(len(s)):
        odd = palinhelper(s, i, i)
        even = palinhelper(s, i, i+1)
        res = max(res, odd, even, key=len)
    
    return res


def longestpalindrome(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1
        
    return res