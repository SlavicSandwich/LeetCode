# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def iterate_through_tree(root, p, q):
            if not root:
                return
            if root.val == q.val or root.val == p.val:
                return root
            if root.val > p.val and root.val > q.val:
                return iterate_through_tree(root.left, p, q)

            if root.val < p.val and root.val < q.val:
                return iterate_through_tree(root.right, p, q)

            if root.val < q.val and root.val > p.val or root.val < p.val and root.val > q.val:
                return root


        return iterate_through_tree(root, p, q)


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.right = TreeNode(9)
root.right.left = TreeNode(7)


print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)