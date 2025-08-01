# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Handle edge case: empty tree
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        # Initialize result list
        result = []
        
        # Add root if not a leaf
        if root.left or root.right:
            result.append(root.val)
        
        # Function to get left boundary (top-down, exclude leaves)
        def getLeftBoundary(node):
            if not node or (not node.left and not node.right):
                return
            result.append(node.val)
            if node.left:
                getLeftBoundary(node.left)
            elif node.right:
                getLeftBoundary(node.right)
        
        # Function to get right boundary (bottom-up, exclude leaves)
        def getRightBoundary(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                getRightBoundary(node.right)
            elif node.left:
                getRightBoundary(node.left)
            result.append(node.val)
        
        # Function to get leaf nodes (left-to-right)
        def getLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
                return
            getLeaves(node.left)
            getLeaves(node.right)
        
        # Traverse boundaries
        getLeftBoundary(root.left)
        # Add leaves, excluding those already in boundaries
        if root.left or root.right:
            getLeaves(root)
        getRightBoundary(root.right)
        
        return result