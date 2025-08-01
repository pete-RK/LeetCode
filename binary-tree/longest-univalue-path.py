# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = [0]
        if not root: return longest[0]

        def dfs(node):
            if not node: return 0

            lefty = dfs(node.left)
            righty = dfs(node.right)

            left = lefty + 1 if node.left and node.left.val == node.val else 0
            right = righty + 1 if node.right and node.right.val == node.val else 0

            longest[0] = max(longest[0], left + right)
            return max(left, right)
        
        dfs(root)

        return longest[0]
            




            
