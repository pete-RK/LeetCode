class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def solve(limit):
            left, diff, count = 0, 0, 0
            counter = defaultdict(int)

            for right in range(len(nums)):
                counter[nums[right]] += 1

                while left <= right and len(counter) > limit:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return solve(k) - solve(k-1)
