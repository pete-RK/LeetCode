# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # first find the mid
        slow, fast, curr = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        def reverse_list(head):
            node = None

            while head:
                temp = head.next
                head.next = node
                node = head
                head = temp
            
            return node
        
        second = slow.next
        slow.next = None
        rev = reverse_list(second)
        
        while curr and rev:
            t1, t2 = curr.next, rev.next
            curr.next = rev
            rev.next = t1
            curr = t1
            rev = t2
        

        return head
            


