# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(root):
            if not root: return 0
            lh, rh = dfs(root.left), dfs(root.right)
            diameter[0] = max(diameter[0], lh+rh)
            return 1 + max(lh, rh)
        
        dfs(root)
        return diameter[0]