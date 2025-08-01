# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sum_set = set()
        check = root

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            curr_sum = node.val + left + right
            if node != check:
                sum_set.add(curr_sum)

            return curr_sum
        
        total_sum = dfs(root)
        if total_sum % 2 != 0: return False

        return total_sum // 2 in sum_set


