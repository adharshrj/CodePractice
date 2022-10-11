from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> int:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mxdtree(self, root:TreeNode):
        if not root:
            return 0
        
        return 1 + max(self.mxdtree(root.left), self.mxdtree(root.right))

    def mxdlo(self, root:TreeNode):
        if not root: return 0

        q = deque([(root, 1)])
        depth = 0

        while q:
            node, d = q.popleft()
            if node.left:
                q.append(node.left, d + 1)
            if node.right:
                q.append(node.right, d + 1)

            depth = max(depth, d)
        
        return depth

test = Solution()
print(test.mxdtree(TreeNode([3,9,20,None,None,15,7])))
        