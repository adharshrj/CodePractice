# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

 
import heapq

# O(n + klogn), o(n)
def kthlargestmax(nums, k):
    nums = [-n for n in nums]
    heapq.heapify(nums)

    for n in range(k-1):
        heapq.heappop(nums)
    
    return -1 * heapq.heappop(nums)

# O(nlogn), O(1)
def kthlargest(nums, k):
    nums.sort()
    return nums[len(nums) - k]


# O(n^2) worst, O(n) avg, O(n) space
def kthlargestqs(nums, k):
    k = len(nums) - k
    def quickselect(l, r):
        if l == r: return nums[l]
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: return quickselect(l, p-1)
        elif p < k: return quickselect(p + 1, r)
        else: return nums[l]
    
    return quickselect(0, len(nums)-1)