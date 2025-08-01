class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_dict = defaultdict(int)
        n = len(s)

        for right in range(n):
            char_dict[s[right]] += 1
            while char_dict and right - left - max(char_dict.values()) >= k:
                char_dict[s[left]] -= 1
                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len