class AllOne:
    """
    Data structure that supports incrementing and decrementing keys' counts,
    and retrieving the keys with maximum and minimum counts in O(1) time.
    Uses a doubly linked list of nodes where each node holds keys with the same count.
    """

    class Node:
        """
        Node in the doubly linked list, representing a frequency count and the keys with that count.
        """
        def __init__(self, count: int):
            self.count = count
            self.keys = set()
            self.prev = None
            self.next = None

    def __init__(self):
        """
        Initialize the AllOne data structure.
        """
        self.key_to_node = {}  # Maps key to its corresponding Node
        self.head = self.Node(0)  # Dummy head node
        self.tail = self.head  # Initially, tail points to head

    def _add_new_node_after(self, prev_node: Node, count: int) -> None:
        """
        Helper to add a new node with the given count after the prev_node.
        """
        new_node = self.Node(count)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        if self.tail == prev_node:
            self.tail = new_node

    def _remove_node(self, node: Node) -> None:
        """
        Helper to remove a node from the linked list.
        """
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.tail == node:
            self.tail = node.prev

    def inc(self, key: str) -> None:
        """
        Increment the count of the key by 1. If the key doesn't exist, add it with count 1.
        """
        if key not in self.key_to_node:
            # Key doesn't exist; add it with count 1 after head if necessary
            if self.head.next is None or self.head.next.count != 1:
                self._add_new_node_after(self.head, 1)
            self.key_to_node[key] = self.head.next
            self.head.next.keys.add(key)
        else:
            # Key exists; move it to the next higher count
            curr = self.key_to_node[key]
            curr_count = curr.count
            if curr.next is None or curr.next.count != curr_count + 1:
                self._add_new_node_after(curr, curr_count + 1)
            curr.next.keys.add(key)
            self.key_to_node[key] = curr.next
            curr.keys.remove(key)
            if not curr.keys:
                self._remove_node(curr)

    def dec(self, key: str) -> None:
        """
        Decrement the count of the key by 1. If the count reaches 0, remove the key.
        """
        if key not in self.key_to_node:
            return  # Key doesn't exist; do nothing

        curr = self.key_to_node[key]
        curr_count = curr.count
        curr.keys.remove(key)

        if curr_count == 1:
            # Count reaches 0; remove the key
            del self.key_to_node[key]
        else:
            # Move to the previous lower count
            if curr.prev == self.head or curr.prev.count != curr_count - 1:
                self._add_new_node_after(curr.prev, curr_count - 1)
            curr.prev.keys.add(key)
            self.key_to_node[key] = curr.prev

        # Remove the current node if it has no more keys
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        """
        Return one of the keys with the maximum count. If no keys, return empty string.
        """
        if self.tail == self.head:
            return ""
        return next(iter(self.tail.keys))

    def getMinKey(self) -> str:
        """
        Return one of the keys with the minimum count. If no keys, return empty string.
        """
        if self.head.next is None:
            return ""
        return next(iter(self.head.next.keys))