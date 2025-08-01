# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if not node:
                return 0, 0
            l1, ld = dfs(node.left, node)
            r1, rd = dfs(node.right, node)

            res[0] = max(res[0], l1+rd+1, ld+r1+1)
            if node.val == parent.val+1:
                return max(l1, r1)+1, 0
            if node.val == parent.val -1:
                return 0, max(ld,rd)+1
            return 0, 0

        res = [0]
        dfs(root, root)
        return res[0]


            

