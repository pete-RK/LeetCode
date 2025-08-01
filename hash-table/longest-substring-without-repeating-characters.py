class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        cache = set()

        for right in range(len(s)):
            while left < right and s[right] in cache:
                cache.remove(s[left])
                left += 1
            
            cache.add(s[right])
            result = max(result, right-left + 1)
        
        return result



        