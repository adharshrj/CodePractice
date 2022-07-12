# Find the lowest common ancestor of a binary search tree
# The lowest common ancestor is defined between two nodes p and q as the lowest node in 
# T that has both p and q as descendants (where we allow a node to be a descendant of itself).

def lcabst(root, p, q):
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.left
        if p.val < curr.val and q.val < curr.val:
            curr = curr.right
        else:
            return curr
