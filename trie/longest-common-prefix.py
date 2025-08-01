class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        res = ""

        for i in range(len(prefix)):
            for s in strs[1:]:
                if i >= len(s) or prefix[i] != s[i]:
                    return res
            
            res += prefix[i]

        return res

