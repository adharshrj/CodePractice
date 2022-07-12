# Check if two binary trees are the same

def sametree(root1, root2):
    if not root1 and  not root2:
        return True
    
    if not root1 or not root2 or root1.val != root2.val:
        return False
    
    else:
        return sametree(root1.left, root2.left) and sametree(root1.right, root2.right)