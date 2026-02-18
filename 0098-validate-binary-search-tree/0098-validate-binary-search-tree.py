# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.isValid = True
        self.inorder(root)
        return self.isValid
    
    def inorder(self, root):
        if root is None or not self.isValid:
            return
        
        self.inorder(root.left)
        
        # Inorder must be strictly increasing
        if self.prev is not None and self.prev >= root.val:
            self.isValid = False
            return
        
        self.prev = root.val
        
        self.inorder(root.right)
