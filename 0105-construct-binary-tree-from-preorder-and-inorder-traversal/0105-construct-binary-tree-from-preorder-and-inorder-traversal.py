# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={}
        for i ,val in enumerate(inorder):
            index[val]=i
        preIndex=0
        def build(left,right):
            nonlocal preIndex
            if left>right:
                return None
            rootval=preorder[preIndex]
            preIndex+=1
            root=TreeNode(rootval)
            mid=index[rootval]
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)
            return root
        return build(0,len(inorder)-1)



        