# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

import math
class AddNumbers:
    def addnumbers(self, l1, l2):
        res = ListNode()
        temp = res
        carry = 0
        while (l1 or l2 or carry == 1):
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
            
            total += carry
            carry = total // 10
            node = ListNode(math.floor(total % 10))
            temp.next = node
            temp = temp.next
        
        return res.next