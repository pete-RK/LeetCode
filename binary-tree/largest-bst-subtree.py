# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.right and not root.left: return 1

        def dfs(node):
            if not node: return 0, float('inf'), float('-inf')

            lh, l_min, l_max = dfs(node.left)
            rh, r_min, r_max = dfs(node.right)

            if l_max < node.val < r_min:
                return lh + rh + 1, min(l_min, node.val), max(r_max, node.val)
            else:
                return max(lh, rh), float('-inf'), float('inf')
            
        return dfs(root)[0]
            
