# Given an array arr[] and an integer K where K is smaller than size of array, 
# the task is to find the Kth smallest element in the given array. 
# It is given that all array elements are distinct.

import heapq


def kthsmallest(nums, k):
    heapq.heapify(nums)
    for i in range(k-1):
        heapq.heappop(nums)
    
    return heapq.heappop(nums)

