# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexs, ind = [], 1
        curr, prev, min_val = head.next, head, float('inf')

        while curr:
            if curr.next:
                if (curr.val < prev.val and curr.val < curr.next.val) or \
                   (curr.val > prev.val and curr.val > curr.next.val):
                    indexs.append(ind)
                    if len(indexs) >= 2:
                        min_val = min(min_val, indexs[-1] - indexs[-2])
            
            ind += 1
            prev, curr = curr, curr.next
        
        if len(indexs) < 2:
            return [-1, -1]

        max_val = indexs[-1] - indexs[0]
        
        return [min_val, max_val]