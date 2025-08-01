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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode node = dummy;

        while (node.next != null && node.next.next != null) {
            ListNode first = node.next, second = node.next.next;

            first.next = second.next;
            node.next = second;
            second.next = first;

            node = first;
        }

        return dummy.next;

    }
}