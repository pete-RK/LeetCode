# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def function(node):
            if node is None:
                return 0, [] 

            l_count, l  = function(node.left)
            r_count, r = function(node.right)

            val = 1 + l_count + r_count 
            v = sorted([node.val] + l + r)[:k]

            if val >= k and sum([node.val > i for i in v]) == k:
                self.count += 1 

            return val, v

        function(root)

        return self.count 

                
                

