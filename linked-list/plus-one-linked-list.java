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
    private int dfs(ListNode head) {
        if (head == null) return 1;

        int total = head.val + dfs(head.next);
        int carry = total / 10;
        head.val = total % 10;

        return carry;
    }
    public ListNode plusOne(ListNode head) {
        int carry = dfs(head);
        if (carry > 0) {
            ListNode newHead = new ListNode(carry);
            newHead.next = head;
            head = newHead;
        }

        return head;
    }
}