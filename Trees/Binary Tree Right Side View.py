# Definition for a binary tree node.
import collections
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level[-1])
        return res






root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
root.right.right.left = TreeNode(4)
root.right.right.right.left = TreeNode(3)

print(Solution().rightSideView(root))
