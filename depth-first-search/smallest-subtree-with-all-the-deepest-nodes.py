# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.deepest = [[], 0]
        queue = deque([(root, 0)])

        def dfs(node):
            if not node or p == node or q == node:
                return node
            
            left, right = dfs(node.left), dfs(node.right)

            if left and right: return node

            return left or right


        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()

                if self.deepest[1] == level:
                    self.deepest[0].append(node)
                elif self.deepest[1] < level:
                    self.deepest[0] = [node]
                    self.deepest[1] = level

                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
        
        if len(self.deepest[0]) == 1:
            return self.deepest[0][0]
        
        else:
            p, q = self.deepest[0][0], self.deepest[0][-1]
            return dfs(root)



