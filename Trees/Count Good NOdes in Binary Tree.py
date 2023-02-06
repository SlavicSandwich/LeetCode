# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def post_order(root:TreeNode, maxi:int):
            if not root:
                return 0

            res = 1 if root.val >= maxi else 0

            res += post_order(root.left, max(maxi, root.val))
            res += post_order(root.right, max(maxi, root.val))

            return res

        return post_order(root, root.val)




