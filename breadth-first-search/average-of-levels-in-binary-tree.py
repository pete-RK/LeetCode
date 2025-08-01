# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root: return res        
        queue = deque([root])

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(statistics.mean(curr))
        
        return res
