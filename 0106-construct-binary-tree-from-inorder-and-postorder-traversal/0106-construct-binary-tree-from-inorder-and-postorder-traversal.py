# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index ={}
        for i,val in enumerate(inorder):
            index[val]=i
        postindex=len(postorder)-1
        def build(left,right):
            nonlocal postindex
            if left>right:
                return None
            rootval=postorder[postindex]
            postindex-=1
            root=TreeNode(rootval)
            mid = index[rootval]
            root.right=build(mid+1,right)
            root.left=build(left,mid-1)
            return root
        return build(0,len(inorder)-1)
        