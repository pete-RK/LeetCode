class RandomizedSet:

    def __init__(self):
        self.res = set()
        
    def insert(self, val: int) -> bool:
        if val in self.res:
            return False

        self.res.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.res:
            return False
        self.res.remove(val)
        return True

    def getRandom(self) -> int:
        if len(self.res) > 0:

            index = random.randrange(0, len(self.res))
            return list(self.res)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()