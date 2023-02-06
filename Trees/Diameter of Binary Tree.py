# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ress = []
        self.get_max_height(root, ress)
        return max(ress) - 1
    def get_max_height(self, root: TreeNode, ress: list):
        if not root:
            return 0
        leftheight = self.get_max_height(root.left, ress)
        rightheight = self.get_max_height(root.right, ress)

        height = 1 + max(leftheight, rightheight)
        diam = 1 + leftheight + rightheight
        ress.append(diam)
        return height



# root = TreeNode(1)
# root.right = TreeNode(3)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)
root.right.left = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print(Solution().diameterOfBinaryTree(root))
