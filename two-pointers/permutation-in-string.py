class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        left, right = 0, len(s1)

        while right <= len(s2):
            counter2 = Counter(s2[left:right])

            if counter1 == counter2: return True
            left +=1 
            right += 1
        
        return False
