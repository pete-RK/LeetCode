# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.possible = []

        queue = deque([self.root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left or not node.right:
                    self.possible.append(node)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)


    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
            return self.root.val

        new_node = TreeNode(val)
        self.possible.append(new_node)
        node = self.possible[0]

        if not node.left:
            node.left = new_node
        elif not node.right:
            node.right = new_node
            self.possible.pop(0)
        
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()