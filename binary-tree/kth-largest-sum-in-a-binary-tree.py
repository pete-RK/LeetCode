# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        heap = []
        queue = deque([root])

        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heappush(heap, -curr_sum)

        for _ in range(k-1):
            if not heap: return -1
            heappop(heap)
        
        if heap:
            return -heappop(heap)
        else:
            return -1
