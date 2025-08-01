# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_max_val_index(self, nums):
        max_val, max_index = 0, 0

        for ind, val in enumerate(nums):
            if val > max_val:
                max_val, max_index = val, ind
        
        return max_val, max_index

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        max_val, max_index = self.get_max_val_index(nums)

        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])

        return root