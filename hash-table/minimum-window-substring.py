class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter2 = Counter(t)
        result = ""
        min_len = math.inf
        left = 0
        counter1 = Counter()

        for right in range(len(s)):
            counter1[s[right]] += 1

            while counter1 >= counter2 and left <= right:
                if right - left + 1 < min_len:
                    result = s[left: right + 1]
                    min_len = right - left + 1
                counter1[s[left]] -= 1
                if counter1[s[left]] == 0:
                    del counter1[s[left]]
                left += 1
        
        return result
            





            


        
        