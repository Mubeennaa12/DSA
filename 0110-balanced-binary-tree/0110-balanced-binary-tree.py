# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if not node:
                return 0
            return max(height(node.left),height(node.right)) +1
        def check(node):
            if not node:
                return True
            left=height(node.left)
            right=height(node.right)
            if abs(left-right)>1:
                return False
            return check(node.left) and check(node.right)
        return check(root)
        

        