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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode first = head, last = head;
        for (int i = 1; i < k ; i++) {
            first = first.next;
        }

        ListNode check = first;
        while (check.next != null) {
            last = last.next;
            check = check.next;
        }

        int temp = first.val;
        first.val = last.val;
        last.val = temp;

        return head;
    }
}