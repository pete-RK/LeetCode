# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        nodes = []

        def dfs(node):
            if not node: return 0
            larger = dfs(node.next)

            if node.val >= larger:
                nodes.append(node.val)
                larger = node.val
            
            return larger
        
        dfs(head)
        prev = None
        for num in nodes:
            newNode = ListNode(num, prev)
            prev = newNode
        
        return newNode

