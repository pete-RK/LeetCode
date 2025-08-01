# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if not list1 or not list2: return list1

        curr = list1
        node1, node2 = None, None
        for i in range(b):
            if i == a-1:
                node1 = curr
            curr = curr.next
        
        node2 = curr.next

        node1.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = node2

        return list1




        