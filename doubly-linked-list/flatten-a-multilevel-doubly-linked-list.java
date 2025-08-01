/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if (head == null) {
            return head;
        }
        Node curr = head;
        while (curr != null) {
            if (curr.child != null) {
                Node temp = curr.next;
                Object[] nodeObject = generateChild(curr.child);
                Node cHead = (Node) nodeObject[0];
                Node cTail = (Node) nodeObject[1];

                curr.next = cHead;
                cHead.prev = curr;
                cTail.next = temp;
                if (temp != null) temp.prev = cTail;
            }
            curr.child = null;
            curr = curr.next;
        }

        return head;
        
    }

    private Object[] generateChild(Node head) {
        Node cHead = head;
        while (head.next != null) {
            head = head.next;
        }
        return new Object[]{cHead, head};
    }
}