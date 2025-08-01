# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd, even = 0, 0
        o, e = head.next, head

        while o:
            if o.val > e.val:
                odd += 1
            elif e.val > o.val:
                even += 1
            if e.next and o.next:
                e, o = e.next.next, o.next.next
            else:
                break
        
        if odd > even: return 'Odd'
        elif even > odd: return 'Even'
        else: return 'Tie'
