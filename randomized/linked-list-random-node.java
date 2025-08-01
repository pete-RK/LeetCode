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
    ListNode head;
    HashMap<Integer, Integer> nodes;
    int listLength = 0;

    public Solution(ListNode head) {
        this.head = head;
        nodes = new HashMap<>();
        traverse();
    }

    private void traverse() {
        ListNode curr = head;

        while (curr != null) {
            nodes.put(listLength, curr.val);
            curr = curr.next;
            listLength++;
        }
    }
    
    public int getRandom() {
        if (listLength == 0) return 0;
        Random rand = new Random();
        int key = rand.nextInt(listLength);

        return nodes.get(key);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */