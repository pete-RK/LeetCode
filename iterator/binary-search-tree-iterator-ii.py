# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder = []
        self.len = 0
        self.pointer = -1
        self.get_in_order(self.root)
    
    def get_in_order(self, node):
        if not node: return

        self.get_in_order(node.left)
        self.inorder.append(node.val)
        self.len += 1
        self.get_in_order(node.right)

    def hasNext(self) -> bool:
        if self.len == 0 or self.pointer == self.len - 1 or self.pointer < -1: return False
        return True

    def next(self) -> int:
        if self.hasNext():
            self.pointer += 1
            return self.inorder[self.pointer]

    def hasPrev(self) -> bool:
        if self.len == 0 or self.pointer <= 0 or self.pointer == self.len: return False
        return True

    def prev(self) -> int:
        if self.hasPrev():
            self.pointer -= 1
            return self.inorder[self.pointer]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()