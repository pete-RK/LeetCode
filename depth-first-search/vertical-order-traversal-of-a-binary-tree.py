# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [[]]
        nodes = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            curr_nodes = defaultdict(list)
            for _ in range(len(queue)):
                node, col = queue.popleft()
                curr_nodes[col].append(node.val)

                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
            
            for key, val in curr_nodes.items():
                nodes[key] += list(sorted(val))
        
        res = []

        for key in sorted(nodes.keys()):
            res.append(nodes[key])
        
        return res

