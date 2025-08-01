class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, max_len = 0, 0
        counter = defaultdict(int)

        for right in range(len(s)):
            counter[s[right]] += 1

            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

        
