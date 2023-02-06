# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def compare_nodes(p, q):
            if not p and not q:
                return True

            if not p and q or not q and p:
                return False

            if p.val == q.val:
                left = compare_nodes(p.left, q.left)
                right = compare_nodes(p.right, q.right)
                return left * right

            return False

        return compare_nodes(p, q)




