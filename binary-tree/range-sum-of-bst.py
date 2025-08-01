# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):
            if not root: return 0

            l, r = dfs(root.left), dfs(root.right)

            curr_sum = l + r
            if root.val in range(low, high+1):
                curr_sum += root.val
            
            return curr_sum
        return dfs(root)