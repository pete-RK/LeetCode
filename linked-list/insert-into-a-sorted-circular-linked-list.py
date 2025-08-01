"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                curr.next = Node(insertVal, curr.next)
                return head
        
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    curr.next = Node(insertVal, curr.next)
                    return head
            
            curr = curr.next
            
            if curr == head:
                break
        
        node.next = head.next
        head.next = node
        return head


