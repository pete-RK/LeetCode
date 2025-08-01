# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def parents(node, par):
            if not node: return 
            if par:
                parent[node] = par
            parents(node.left, node)
            parents(node.right, node)
        
        parents(root, None)

        visited = set()
        q = deque([target])
        visited.add(target)
        dist = 0

        while q:
            if dist == k:
                return [node.val for node in q]
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left, node.right, parent.get(node)):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            dist += 1

        return []
