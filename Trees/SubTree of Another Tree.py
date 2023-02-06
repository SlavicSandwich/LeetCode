# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def traverse_tree(root: TreeNode, subRoot: TreeNode):
            if not root:
                return False
            if root.val == subRoot.val:
                if compare_nodes(root, subRoot):
                    return True


            right = traverse_tree(root.right, subRoot)
            left = traverse_tree(root.left, subRoot)

            return right or left

        def compare_nodes(p: TreeNode, q: TreeNode):
            if not p and not q :
                return True

            if q and not p or p and not q:
                return False

            if p.val == q.val:
                left = compare_nodes(p.left, q.left)
                right = compare_nodes(p.right, q.right)
                return left * right

            return False

        return traverse_tree(root, subRoot)


root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)
tochek = TreeNode(4)
tochek.left = TreeNode(1)
tochek.right = TreeNode(2)

print(Solution().isSubtree(root, tochek))
