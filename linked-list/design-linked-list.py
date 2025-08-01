class Node:

    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        # If the list was empty, head is also tail
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            # If list is empty, head and tail both become new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            # Insert new_node after prev
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        # If deleting the head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            # If that was the only node, tail also needs to be None
            if self.size == 0:
                self.tail = None
            return
        
        # Otherwise, find the node before the one to delete
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        
        # Remove prev.next from the chain
        to_delete = prev.next
        prev.next = to_delete.next
        self.size -= 1

        # If deleting the tail, update self.tail
        if index == self.size:  # Because we just decremented size
            self.tail = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)