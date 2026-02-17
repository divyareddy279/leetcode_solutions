from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            level = []
            
            for _ in range(level_size):
                curr = q.popleft()
                level.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            result.append(level)
        
        return result
