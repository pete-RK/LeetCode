# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([(1, root)])
        min_level, min_val = 1, root.val
        level = 1

        while queue:
            total_sum = 0
            for _ in range(len(queue)):
                level, node = queue.popleft()
                total_sum += node.val

                if node.left:
                    queue.append((level+1, node.left))
                if node.right:
                    queue.append((level+1, node.right))
            
            if total_sum < min_val:
                min_level, min_val = level, total_sum
        
        return min_level
