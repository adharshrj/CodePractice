# Given some points in an x-y plane find the k closest points to the origin

# Use MinHeap

import heapq


def kclosest(points, k):
    ptsStore = []
    for x, y in points:
        distance = (x-0)**2 + (y-0)**2
        ptsStore.append([distance, x, y])
    heapq.heapify(ptsStore)

    closest = []
    while k > 0:
        distance, x, y = heapq.heappop(ptsStore)
        closest.append([x, y])
        k-=1

    return closest