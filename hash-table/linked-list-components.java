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
    public int numComponents(ListNode head, int[] nums) {
        if (head == null) return 0;
        Set<Integer> numSet = new HashSet<>();
        int res = 0;

        for (int num : nums) {
            numSet.add(num);
        }

        while (head != null) {
            if (numSet.contains(head.val)) {
                while (head != null && numSet.contains(head.val)) {
                    head = head.next;
                }
                res += 1;
            } else {
                head = head.next;
            }
        }

        return res;
    }
}