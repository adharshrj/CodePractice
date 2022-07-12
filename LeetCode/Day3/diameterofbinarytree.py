# Find the diameter of the given binary tree
# Diameter is the distance between the left most and right most node.

def treediameter(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1
        
        left, right = dfs(root.left), dfs(root.right)
        res[0] = max(res[0], 2 + left + right)

        return 1 + max(left, right)
    
    dfs(root)
    return res[0]
