# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
#     Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#     Output: [[1,6],[8,10],[15,18]]
#     Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def mergeintervals(intervals):
    intervals.sort()
    i = 0
    while i < len(intervals)-1:
        if intervals[i][1] >= intervals[i+1][0]:
            if intervals[i][1] < intervals[i+1][1]:
                intervals[i][1] = intervals[i+1][1]
            
            intervals.remove(intervals[i+1])
        
        else:
            i+=1
    
    return intervals