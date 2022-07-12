# Mirror/invert the given binary tree

def inverttree(root):
    if not root:
        return root
    
    if root:
        root.left, root.right = root.right, root.left
        inverttree(root.left)
        inverttree(root.right)
    
    return root