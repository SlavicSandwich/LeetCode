# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        n = 0
        return self.iterate(root, n)


    def iterate(self, root:TreeNode, n:int):
        if not root:
            return n
        n += 1
        res = max(self.iterate(root.right, n), self.iterate(root.left, n))
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxDepth(root))




