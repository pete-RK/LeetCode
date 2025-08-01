# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        if not root:
            return [[] for _ in queries]
        
        nodes = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        def find_closest_values(val):
            # Initialize min and max values
            min_val = max_val = -1
            left, right = 0, len(nodes) - 1
            
            # Binary search for largest value <= val
            while left <= right:
                mid = left + (right - left) // 2
                if nodes[mid] == val:
                    return [val, val]
                elif nodes[mid] < val:
                    min_val = nodes[mid]
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Binary search for smallest value >= val
            left, right = 0, len(nodes) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nodes[mid] == val:
                    return [val, val]
                elif nodes[mid] > val:
                    max_val = nodes[mid]
                    right = mid - 1
                else:
                    left = mid + 1
            
            return [min_val, max_val]
        
        result = []
        for query in queries:
            result.append(find_closest_values(query))
        
        return result