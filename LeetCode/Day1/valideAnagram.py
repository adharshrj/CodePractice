# Given two strings check if they are anagrams of each other
# Ex anagram and nagaram
# Use hashmaps / dictionary

def validanagram(s, t):
    if len(s)!=len(t):
        return False

    smap = {}
    tmap = {}

    for ch in s:
        if ch in smap:
            smap[ch] += 1
        else:
            smap[ch] = 1
    
    for ch in t:
        if ch in tmap:
            tmap[ch] += 1
        else:
            tmap[ch] = 1
    
    for key in smap:
        if key not in tmap or smap[key] != tmap[key]:
            return False
    return True

print(validanagram("anagram", "nagaram"))
print(validanagram("anagram", "nasgaram"))