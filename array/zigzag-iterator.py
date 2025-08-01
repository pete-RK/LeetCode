class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.array = self.get_deque(v1, v2)
    
    def get_deque(self, v1, v2):
        array = []
        i = j = 0

        while i < len(v1) and j < len(v2):
            if i == j:
                array.append(v1[i])
                i += 1
            else:
                array.append(v2[j])
                j += 1
        
        if i < len(v1):
            array.extend(v1[i:])
        if j < len(v2):
            array.extend(v2[j:])
        
        return deque(array)

    def next(self) -> int:
        return self.array.popleft()

    def hasNext(self) -> bool:
        return True if self.array else False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())