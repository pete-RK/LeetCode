/**
 * Definition for polynomial singly-linked list.
 * class PolyNode {
 *     int coefficient, power;
 *     PolyNode next = null;
 
 *     PolyNode() {}
 *     PolyNode(int x, int y) { this.coefficient = x; this.power = y; }
 *     PolyNode(int x, int y, PolyNode next) { this.coefficient = x; this.power = y; this.next = next; }
 * }
 */

class Solution {
    public PolyNode addPoly(PolyNode p1, PolyNode p2) {
        if (p1 == null && p2 == null) return null;
        PolyNode dummy = new PolyNode();
        PolyNode prev = dummy;

        while (p1 != null && p2 != null) {
            PolyNode curr = new PolyNode();
            PolyNode n1 = p1, n2 = p2;
            if (p1.power == p2.power) {
                p1 = p1.next; p2 = p2.next;
                int val = n1.coefficient + n2.coefficient;
                if (val == 0) continue;
                curr.coefficient = val;
                curr.power = n1.power;
            } else if (p1.power > p2.power) {
                p1 = p1.next;
                curr.coefficient = n1.coefficient;
                curr.power = n1.power;
            } else {
                p2 = p2.next;
                curr.coefficient = n2.coefficient;
                curr.power = n2.power;
            }

            prev.next = curr;
            prev = curr;
        }

        if (p1 != null) prev.next = p1;
        if (p2 != null) prev.next = p2;

        return dummy.next;
    }
}