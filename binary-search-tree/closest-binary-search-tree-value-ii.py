# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nodes = []

        def dfs(root):
            nonlocal nodes
            if not root: return

            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
        
        dfs(root)
        l, r = 0, len(nodes)-k

        while l < r:
            mid = l + (r-l)//2

            if target - nodes[mid] > nodes[mid+k] - target:
                l = mid + 1
            else:
                r = mid
        
        return nodes[l:l+k]





        