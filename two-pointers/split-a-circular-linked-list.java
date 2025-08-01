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
    public ListNode[] splitCircularLinkedList(ListNode head) {
        ListNode slow = head, fast = head.next;

        while (fast.next != head) {
            slow = slow.next;
            if (fast.next.next != head) fast = fast.next.next;
            else fast = fast.next;
        }

        ListNode newNode = slow.next;
        slow.next = head;
        fast.next = newNode;

        return new ListNode[] {head, newNode};
    }
}