class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits)) <= 2: return len(fruits)

        counter = defaultdict(int)
        left, max_count = 0, 0

        for right in range(len(fruits)):
            counter[fruits[right]] += 1

            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count

