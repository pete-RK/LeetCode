class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2== 0:
                nums[i] = 0
            else:
                nums[i] = 1
        return self.atMost(nums, goal)- self.atMost(nums, goal-1)

    def atMost(self, nums: List[int], goal: int) -> int:
        head, tail, total, result = 0, 0, 0, 0
        for head in range(len(nums)):
            total += nums[head]
            while total > goal and tail <= head:
                total -= nums[tail]
                tail += 1
            result += head - tail + 1
        return result