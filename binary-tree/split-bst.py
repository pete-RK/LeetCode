# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        
        if root.val <= target:
            # Node goes to smaller tree, split right subtree
            smaller, larger = self.splitBST(root.right, target)
            root.right = smaller
            return [root, larger]
        else:
            # Node goes to larger tree, split left subtree
            smaller, larger = self.splitBST(root.left, target)
            root.left = larger
            return [smaller, root]
