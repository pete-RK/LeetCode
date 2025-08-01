class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) < 4 or len(s) > 12:
            return res


        def backtrack(ind, parts):
            if len(parts) == 4 and ind >= len(s):
                res.append(".".join(parts[:]))
                return
            
            if len(parts) > 4:
                return
            
            for l in range(1, 4):
                if ind + l <= len(s):
                    part = s[ind: ind+l]
                    if (part[0] =="0" and len(part) > 1) or int(part)> 255:
                        continue
                    backtrack(ind + l, parts + [part])
            
        backtrack(0, [])

        return res
            

            

        