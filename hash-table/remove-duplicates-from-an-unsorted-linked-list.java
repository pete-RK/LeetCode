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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        Set<Integer> seen = new HashSet<>(), deleted = new HashSet<>();
        ListNode curr = head;

        while (curr != null) {
            if (seen.contains(curr.val)) {
                deleted.add(curr.val);
            }
            seen.add(curr.val);
            curr = curr.next;
        }

        ListNode prev = null;
        ListNode node = head;

        while (node != null) {
            if (deleted.contains(node.val)) {
                if (prev != null) {
                    prev.next = node.next;
                } else {
                    head = head.next;
                }
            } else {
                prev = node;
            }
            node = node.next;
        }

        return head;

    }
}