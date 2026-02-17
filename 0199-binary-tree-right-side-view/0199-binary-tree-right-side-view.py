# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.rightView(root, 0, res)
        return res
    
    def rightView(self, root, level, res):
        if root is None:
            return
        
        # If this is first node of this level
        if level == len(res):
            res.append(root.val)
        
        # Visit right first
        self.rightView(root.right, level + 1, res)
        self.rightView(root.left, level + 1, res)
