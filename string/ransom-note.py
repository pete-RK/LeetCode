class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cm = Counter(magazine)
        cr = Counter(ransomNote)

        for w in cr:
            if cr[w] > cm[w]:
                return False
        
        return True

        