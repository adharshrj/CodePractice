# Check if the last node of linked list is connected to the first.
#Floyd's circle finding algorithm

def hascycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False