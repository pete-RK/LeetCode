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
    public int pairSum(ListNode head) {
        if (head == null) return 0;
        int result = 0;
        ListNode slow = head, fast = head;
        ListNode prev = null;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        if (prev != null) prev.next = null;
        ListNode head2 = reverse(slow);

        while (head != null) {
            result = Math.max(result, head.val + head2.val);
            head = head.next;
            head2 = head2.next;
        }

        return result;
    }

    private ListNode reverse(ListNode root) {
        ListNode node = null;

        while (root != null) {
            ListNode temp = root.next;
            root.next = node;
            node = root;
            root = temp;
        }

        return node;
    }
}