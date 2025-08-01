# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            if node1.val != node2.val:return False
            if not node1.left and not node2.left and not node1.right and not node2.right:
                return True

            return (dfs(node1.left, node2.left) and dfs(node1.right, node2.right)) or (dfs(node1.left, node2.right) and dfs(node1.right, node2.left))
        
        return dfs(root1, root2)