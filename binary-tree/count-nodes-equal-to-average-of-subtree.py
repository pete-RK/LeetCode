# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root):
            if not root: return 0, 0

            lh, lc = dfs(root.left)
            rh, rc = dfs(root.right)

            curr_val = lh + rh + root.val 
            curr_count = lc + rc + 1
            if root.val == (curr_val) // (curr_count):
                self.count += 1

            return curr_val, curr_count
        
        dfs(root)
        return self.count
