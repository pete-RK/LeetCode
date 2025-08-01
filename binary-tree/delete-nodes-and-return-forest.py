# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        if not root: return [root]
        res = []

        def dfs(root):
            if not root: return 

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_del:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                return None
            
            return root
        
        
        if dfs(root):
            res.append(root)
        return res

