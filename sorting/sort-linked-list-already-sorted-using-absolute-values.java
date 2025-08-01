/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortLinkedList(ListNode head) {
        if (head == null) return head;
        ListNode dummy = new ListNode(0, head);
        ListNode curr = head, prev = null;

        while (curr != null) {
            if (curr.val < 0) {
                if (prev != null) {
                    prev.next = curr.next;
                    ListNode temp = dummy.next;
                    dummy.next = curr;
                    curr.next = temp;
                    curr = prev.next;
                } else {
                    prev = curr;
                    curr = curr.next;
                }
            } else {
                prev = curr;
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}