# Balanced binary tree = a binary tree in which the left and right subtrees of 
# every node differ in height by no more than 1.
def dfs(root):
        if not root:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1]) ]

def balancedtree(root):
    return dfs(root)[0]