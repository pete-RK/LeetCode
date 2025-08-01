class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        dp[0] = {0}

        for st in stones:
            for jp in dp[st]:
                for dis in [jp-1, jp, jp+1]:
                    if dis > 0 and st + dis in dp:
                        dp[st + dis].add(dis)
        
        return len(dp[stones[-1]]) > 0


        