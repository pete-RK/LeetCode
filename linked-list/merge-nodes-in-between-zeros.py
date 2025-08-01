# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr_sum = 0
        head = head.next
        dummy = ListNode(-1)
        prev = dummy
        while head:
            if head.val == 0:
                newNode = ListNode(curr_sum)
                prev.next = newNode
                prev = newNode
                curr_sum = 0

            curr_sum += head.val
            head = head.next
        
        return dummy.next

            