# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        self.in_order(root)
    
    def in_order(self, root):
        if not root: return

        self.in_order(root.left)
        self.tree.append(root.val)
        self.in_order(root.right)
        
    def next(self) -> int:
        val = self.tree[0]
        del self.tree[0]

        return val

    def hasNext(self) -> bool:
        return len(self.tree) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()