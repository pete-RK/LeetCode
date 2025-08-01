class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        queue = deque([(beginWord, 1)])
        min_dist = float('inf')

        while queue:
            for _ in range(len(queue)):
                word, dist = queue.popleft()
                if word == endWord:
                    return dist
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char == word[i]:
                            continue
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordSet:
                            queue.append((new_word, dist+1))
                            wordSet.remove(new_word)
            
        return 0
            




        