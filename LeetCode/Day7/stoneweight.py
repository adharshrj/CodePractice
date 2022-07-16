# Given an array iterate through it and replace the 1st and 2nd largest numbers with their difference.

# Use maxheap

import heapq


def stoneweight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)
    
    stones.append(0)
    return abs(stones[0])


print(stoneweight([2,7,4,1,8,1]))