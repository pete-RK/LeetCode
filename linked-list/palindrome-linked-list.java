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
    public ListNode reverse(ListNode head){
        ListNode node = null;

        while (head != null){
            ListNode temp = head.next;
            head.next = node;
            node = head;
            head = temp;
        }
        return node;
    }
    public boolean isPalindrome(ListNode head) {
        if (head == null) return true;
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode mid = reverse(slow);

        while(mid != null){
            if (mid.val != head.val) {
                return false;
            }
            mid = mid.next;
            head = head.next;
        }
        return true;
    }
}