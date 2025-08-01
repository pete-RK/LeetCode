# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head: return []

        length = 0
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
            length += 1
        
        res = [0]*length
        stack = []

        for ind, num in enumerate(nodes):
            while stack and nodes[stack[-1]] < num:
                res[stack.pop()] = num
                
            stack.append(ind)
        
        return res






        