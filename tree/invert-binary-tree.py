# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        if not root.left and not root.right: return root

        if root.left and root.right:
            root.right, root.left = root.left, root.right
        elif root.left and not root.right:
            root.left, root.right = None, root.left
        else:
            root.left, root.right = root.right, None
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        