# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        ans = 0
        seen = set()

        def dfs(node):
            if not node: return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                seen.add(node)

                for nei in graph[node]:
                    if nei not in seen:
                        queue.append(nei)
            
            ans += 1
        
        return ans - 1


