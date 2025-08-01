# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Dummy node pointing at the start of the sorted list
        dummy = ListNode(0)
        dummy.next = head

        # 'curr' will traverse the list, looking for out-of-order nodes to insert
        curr = head

        while curr and curr.next:
            # If the current node is in correct order relative to the next node, just move on
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                # 'to_insert' is the node we need to relocate
                to_insert = curr.next
                # detach 'to_insert' from the list
                curr.next = curr.next.next

                # Find where 'to_insert' belongs in the sorted portion (dummy->...->curr)
                prev = dummy
                while prev.next and prev.next.val < to_insert.val:
                    prev = prev.next
                
                # Insert 'to_insert' after 'prev'
                to_insert.next = prev.next
                prev.next = to_insert

        return dummy.next


