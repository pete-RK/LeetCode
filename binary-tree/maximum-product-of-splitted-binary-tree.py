# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_total(self, root):
        if not root: return 0

        lh = self.get_total(root.left)
        rh = self.get_total(root.right)

        total = lh + rh + root.val

        return total

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.get_total(root)
        self.max_val = 0

        def dfs(root):
            if not root: return 0

            curr_sum = root.val + dfs(root.left) + dfs(root.right)
            self.max_val = max(self.max_val, (self.total - curr_sum)*(curr_sum))
            return curr_sum
        
        dfs(root)

        return self.max_val % (10 **9 + 7)
