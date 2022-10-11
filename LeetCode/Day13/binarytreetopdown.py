from collections import deque


class TreeNode:
    def __init__(self, val = None, left = None, right = None) -> int:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def topdown(self, root: TreeNode):
        if not root: return []

        q = deque([(root)])
        l, r = [], []

        while q:
            level = []
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            l.append(level[0])
            r.append(level[-1])
        
        return (l[::-1] + r[1:])

# May or may not be correct
