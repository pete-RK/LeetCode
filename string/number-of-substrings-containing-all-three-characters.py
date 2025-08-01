class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, count = 0, 0
        char_dict = defaultdict(int)

        for right in range(len(s)):
            char_dict[s[right]] += 1
            while len(char_dict) == 3:
                count += len(s) - right
                char_dict[s[left]] -= 1

                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1
            
        return count