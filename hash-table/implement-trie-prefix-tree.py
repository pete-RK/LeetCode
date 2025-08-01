class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')
            if index not in node.children:
                node.children[index] = Node()
            node = node.children[index]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if index not in node.children:
                return False
            node = node.children[index]  
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if index not in node.children:
                return False
            node = node.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)