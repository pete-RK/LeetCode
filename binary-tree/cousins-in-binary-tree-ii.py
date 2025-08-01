# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        queue = deque([(root.val, root)])

        while queue:
            level_sum = 0
            for local_sum, node in queue:
                level_sum += node.val
            
            for _ in range(len(queue)):
                local_sum, node = queue.popleft()
                child_sum = 0
                if node.left: child_sum += node.left.val
                if node.right: child_sum += node.right.val

                if node.left: queue.append((child_sum, node.left))
                if node.right: queue.append((child_sum, node.right))

                node.val = level_sum - local_sum
        
        return root

                



                




