class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge(left, right):
            result = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        def count_pairs(left, right):
            count = 0
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > right[j] * 2:
                    count += len(left) - i
                    j += 1  
                else:
                    i += 1 
            
            return count

        def merge_sort_with_count(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, left_count = merge_sort_with_count(nums[:mid])
            right, right_count = merge_sort_with_count(nums[mid:])
            merged = merge(left, right)
            merge_count = count_pairs(left, right)
            total_count = left_count + right_count + merge_count
            return merged, total_count
        
        _, count = merge_sort_with_count(nums)
        return count
        
