# Validate a binary search tree given its root
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

def validbst(root):
    def validation(node, minv, maxv):
        if not node:
            return True

        if node.val <= minv or node.val >= maxv:
            return False
        
        else:
            return validation(node.left, minv, node.val) and validation(root.right, node.val, maxv)
    
    return validation(root, float('-inf'), float('inf'))