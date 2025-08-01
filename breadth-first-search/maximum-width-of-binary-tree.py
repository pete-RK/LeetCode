# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val = 0
        if not root: return max_val
        queue = deque([(0, root)])

        while queue:
            maxi, mini = -math.inf, math.inf
            for _ in range(len(queue)):
                level, node = queue.popleft()
                if level < mini: mini = level
                elif level > maxi: maxi = level

                if node.left:
                    queue.append((2*level+1, node.left))
                if node.right:
                    queue.append((2*level+2, node.right))
            
            if not (maxi == -math.inf or mini == math.inf or maxi == mini):
                max_val = max(max_val, abs(maxi - mini))
        
        return max_val + 1
                
                

