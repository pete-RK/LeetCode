class Solution:
    def clearStars(self, s: str) -> str:
        ans, heap = [*s], []


        for i, c in enumerate(s):
            if c == "*": ans[i] = ans[-heappop(heap)[1]] = ''
            else: heappush(heap,(c,-i))
        
        return ''.join(ans)


        

