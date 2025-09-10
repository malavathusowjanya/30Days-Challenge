# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,l):
        if root==None:
            return
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
    def inorderTraversal(self, root):
        l=[]
        self.inorder(root,l)
        return l
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        