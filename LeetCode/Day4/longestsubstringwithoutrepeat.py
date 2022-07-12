# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#     Input: s = "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with the length of 3.

def longest(s):
    l = 0
    res = 0
    hs = set()

    for r in range(len(s)):
        while s[r] in hs:
            hs.remove(s[l])
            l+=1
        hs.add(s[r])
        res = max(res, r-l+1)
    
    return res