# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.reverse(root)
        return root

    def reverse(self, root:TreeNode):
        if not root:
            return
        root.right, root.left = root.left, root.right
        self.reverse(root.right)
        self.reverse(root.right)

