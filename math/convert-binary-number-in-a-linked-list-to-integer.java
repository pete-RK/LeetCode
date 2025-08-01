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
    private int[] dfs(ListNode head) {
        if (head == null) return new int[]{0, 0};

        int[] nextResult = dfs(head.next);
        int currSum = nextResult[0];
        int power = nextResult[1];

        if (head.val == 1) {
            currSum += 1 << power;
        }
        return new int[]{currSum, power + 1};
    }

    public int getDecimalValue(ListNode head) {
        if (head == null) return 0;
        return dfs(head)[0];
    }
}