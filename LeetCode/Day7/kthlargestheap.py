# Find the Kth largest element in an array
# Use minHeap

import heapq
class KthLargest:
    def __init__(self, nums, k) -> None:
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        if (len(self.minHeap) > k):
            heapq.heappop(self.minHeap)
    
    def add(self, val) -> int:
        heapq.heappush(self.minHeap, val)
        if (len(self.minHeap) > self.k):
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

