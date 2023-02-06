# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root):
            if not root:
                return [0, True]

            leftheight = get_height(root.left)
            rightheight = get_height(root.right)

            if leftheight[1] is False or rightheight[1] is False or abs(leftheight[0] - rightheight[0]) > 1:
                return [-1, False]

            height =1 + max(leftheight[0], rightheight[0])
            return [height, True]

        return get_height(root)[1]



