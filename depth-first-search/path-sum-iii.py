# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = {0:1}

        def dfs(node, curr_sum):
            if not node: return 0

            curr_sum += node.val
            num_paths = prefix_sum.get(curr_sum - targetSum, 0)

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            num_paths += dfs(node.left, curr_sum)
            num_paths += dfs(node.right, curr_sum)

            prefix_sum[curr_sum] -= 1
        
            return num_paths
        
        return dfs(root, 0)