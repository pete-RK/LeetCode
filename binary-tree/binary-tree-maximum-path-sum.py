# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -math.inf
        
        def dfs(node):
            nonlocal max_path
            if not node: return 0
            
            lh = max(dfs(node.left), 0)
            rh = max(dfs(node.right), 0)
            
            curr = node.val + lh + rh
            
            max_path = max(max_path, curr)
            
            return node.val + max(lh, rh)
        
        dfs(root)
        return max_path