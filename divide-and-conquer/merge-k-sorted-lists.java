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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        ListNode dummy = new ListNode(0);

        for (ListNode l : lists) {
            ListNode curr = merge(dummy.next, l);
            dummy.next = curr;
        }

        return dummy.next;
    }

    private ListNode merge(ListNode l1, ListNode l2){
        ListNode node = new ListNode(0);
        ListNode ans = node;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                node.next = l1;
                l1 = l1.next;
            } else {
                node.next = l2;
                l2 = l2.next;
            }
            node = node.next;
        }

        if (l1 != null) node.next = l1;
        else node.next = l2;

        return ans.next;
    }
}