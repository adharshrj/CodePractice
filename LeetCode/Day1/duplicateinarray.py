# Example input [1, 2, 4, 6, 1]
# Use a set

def containsdupliate(nums):
    hs = set()
    for n in nums:
        if n in hs:
            return True
        hs.add(n)
    return

arr = [1, 2, 4, 6, 1]
print(containsdupliate(arr))