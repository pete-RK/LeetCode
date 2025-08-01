class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target = target[::-1]

        for i in range(1, n+1):
            if target[-1] == i:
                res.append("Push")
                target.pop()
            else:
                res += ["Push", "Pop"]
            
            if not target: break
        
        return res