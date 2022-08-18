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

test = Solution()
print(test.mxdtree(TreeNode([3,9,20,None,None,15,7])))
        