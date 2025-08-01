class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def find_peak(arr):

            stack, acc = [], 0
            peeks = []

            for height in arr:
                count = 1
                while stack and height <= stack[-1][0]:
                    h, c = stack.pop()
                    acc -= h * c
                    count += c
                stack.append((height, count))
                acc += height * count
                peeks.append(acc)
            return peeks

        fwd = [0] + find_peak(maxHeights)
        rev = find_peak(maxHeights[::-1])[::-1] + [0]

        return max(f + r for f, r in zip(fwd, rev))





