# Given 2 linked list merge them in sorted order

def mergelinkedlist(h1, h2):
    temp = ListNode()
    tail = temp
    while h1 and h2:
        if h1.val < h2.val:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next
    
    if h1:
        tail.next = h1
    
    if h2:
        tail.next = h2
    
    return temp.next

