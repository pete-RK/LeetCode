class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        
        # Max heap based on frequency
        heap = []
        for char, freq in counter.items():
            heapq.heappush(heap, (-freq, char))
        
        prev = None  # Previously used character and its remaining count
        res = []
        
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if freq < -1:
                prev = (freq + 1, char)  # Decrement frequency and store for next round
        
        return ''.join(res) if not prev else ""

