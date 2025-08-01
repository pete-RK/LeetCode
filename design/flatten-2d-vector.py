class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vector = []
        for i in range(len(vec)-1, -1, -1):
            self.vector += vec[i][::-1]
        self.vector[::-1]

    def next(self) -> int:
        return self.vector.pop()

    def hasNext(self) -> bool:
        return True if self.vector else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()