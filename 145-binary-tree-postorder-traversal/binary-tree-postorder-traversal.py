# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self,root,l):
        if root==None:
            return
        self.postorder(root.left,l)
        self.postorder(root.right,l)
        l.append(root.val)
    def postorderTraversal(self, root):
        l=[]
        self.postorder(root,l)
        return l
   
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        