# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        sizes = []

        def dfs(node):
            if not node: return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            size = 1 + lh + rh
            if lh != rh: return -1

            sizes.append(size) 
            return 1 + lh + rh
        
        dfs(root)
        sizes.sort(reverse=True)

        return sizes[k-1] if k <= len(sizes) else -1
            

