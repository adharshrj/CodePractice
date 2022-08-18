#  Given an array, separate them into arrays of anagrams and return

from collections import defaultdict


def groupanagram(arr):
    hm = defaultdict(list)

    for s in arr:
        hm[str(sorted(s))].append(s)
    
    return hm.values()

print(groupanagram(["eat","tea","tan","ate","nat","bat"]))