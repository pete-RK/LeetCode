class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')
            if index not in node.children:
                node.children[index] = Trie()
            node = node.children[index]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, ind):
            if ind == len(word):
                return node.end
            char = word[ind]
            if char == '.':
                return any(dfs(child, ind+1) for child in node.children.values())
            index = ord(char) - ord('a')
            if index not in node.children:
                return False
            return dfs(node.children[index], ind+1)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)