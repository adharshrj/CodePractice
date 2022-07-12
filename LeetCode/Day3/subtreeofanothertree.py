# Given two tree check if one tree is a subtree of the other

def sametree(p, q):
    if not p and not q:
        return True
    
    if p and q and p.val == q.val:
        return sametree(p.left, q.left) and sametree(p.right, q.right)

def subtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False
    
    if sametree(root, subroot):
        return True
    
    return subtree(root.left, subroot) or subtree(root.right, subroot)