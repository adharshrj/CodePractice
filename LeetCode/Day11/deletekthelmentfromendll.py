# Delete the kth element from the end of likned list
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deletekth(self, head: ListNode, k):
        d = ListNode(0, head)
        l , r = d, head

        while k > 0 and r:
            r = r.next
            k -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return d.next

test = Solution()
print(test.deletekth([1,2,3,4,5], 2))