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
    Deque<Integer> q1 = new ArrayDeque<>(), q2 = new ArrayDeque<>();

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode c1 = l1, c2 = l2;

        while (c1 != null) {
            q1.add(c1.val);
            c1 =c1.next;
        } while (c2 != null) {
            q2.add(c2.val);
            c2 =c2.next;
        }

        int carry = 0;
        ListNode dummyHead = null;

        while (!q1.isEmpty() || !q2.isEmpty() || carry != 0) {
            int v1 = 0, v2 = 0;
            if (!q1.isEmpty()) v1 = q1.pollLast();
            if (!q2.isEmpty()) v2 = q2.pollLast();

            int total = v1 + v2 + carry;
            carry = total / 10;

            ListNode newNode = new ListNode(total % 10);
            newNode.next = dummyHead;
            dummyHead = newNode;
        }
        return dummyHead;
    }
}