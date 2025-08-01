class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]




