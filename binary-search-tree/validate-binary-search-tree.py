# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, minV, maxV):
            if not node: return True

            if not(node.val > minV and node.val < maxV):
                return False
            
            return valid(node.left, minV, node.val) and valid(node.right, node.val, maxV)
        
        return valid(root, float('-inf'), float('inf'))

            

        