# Find the max depth of the given binary tree:


def maxdepth(root):
    if not root:
        return 0
    
    return 1 + max(maxdepth(root.left), maxdepth(root.right))