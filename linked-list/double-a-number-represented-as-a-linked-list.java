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
    public ListNode doubleIt(ListNode head) {
        if (head == null) return head;
        int carry = dfs(head);

        if (carry > 0){
            ListNode newHead = new ListNode(carry, head);
            return newHead;
        }

        return head;
    }

    private int dfs(ListNode node) {
        if (node == null) return 0;

        int carry = dfs(node.next);
        int newVal = (2*node.val) + carry;
        int digit = newVal%10;

        node.val = digit;
        return newVal/10;
    }
}