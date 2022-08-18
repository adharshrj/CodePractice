import heapq


def klargest(nums, k):
    nums = [-n for n in nums]
    res = []
    heapq.heapify(nums)
    while k > 0:
        res.append(-1 * heapq.heappop(nums))
        k-=1
    return res