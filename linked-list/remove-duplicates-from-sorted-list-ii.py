# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        dummy = ListNode(0,head)
        curr = dummy

        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                temp = curr.next
                num = temp.val

                while temp and temp.val == num:
                    temp = temp.next
                
                curr.next = temp
            else:
                curr = curr.next
        
        return dummy.next



        

        