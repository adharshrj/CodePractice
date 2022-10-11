def longestsub(s: str, k: int):
    start, mx, frq = 0, float('-inf'), {}
    
    for end in range(len(s)):
        right = s[end]
        if right not in frq:
            frq[right] = 0
        frq[right] += 1

        while len(frq) > k:
            left = s[start]
            frq[left] -= 1
            if frq[left] == 0:
                del frq[left]
            start += 1
        
        mx = max(mx, end - start + 1)

    return mx

print(longestsub("araaci", 2))