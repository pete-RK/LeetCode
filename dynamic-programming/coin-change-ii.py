class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def recursion(ind, target):
            if ind < 0 or target < 0: return 0
            if ind == 0:
                if target % coins[ind] == 0: return 1
            if (ind, target) in memo:
                 return memo[(ind, target)]
            take = 0
            if target >= coins[ind]:
                take = recursion(ind, target - coins[ind])
            no_take = recursion(ind-1, target)

            memo[(ind, target)] = take + no_take

            return memo[(ind, target)]
        
        return recursion(len(coins)-1, amount)
