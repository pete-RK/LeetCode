# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, s):
            if not node: return
            
            if not node.right and not node.left:
                s += str(node.val)
                res.append(s)
            
            s += str(node.val) + "->"
            dfs(node.left, s)
            dfs(node.right, s)
        
        dfs(root, "")

        return res