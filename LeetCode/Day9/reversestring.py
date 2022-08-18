# Reverse the given strng

def reverse(s):
    s.strip()
    s.split(" ")
    op = []
    l, r = 0, len(s) - 1
    while l < r:
        s[l],s[r] = s[r], s[l]
        l += 1
        r -= 1
    
    for i in s:
        if i == "": continue
        else: op.append(i)
    
    return " ".join(op)