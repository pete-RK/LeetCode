class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0

        for i in range(len(nums)-1):
            part1 = sum(nums[:i])
            part2 = total - part1

            if abs(part1 - part2) % 2 == 0:
                count += 1
        
        return count

            