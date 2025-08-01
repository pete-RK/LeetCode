class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            row = matrix[i]

            if row[-1] < target: continue
            if row[0] > target: break

            l, r = 0, len(row) - 1

            while l <= r:
                mid = l+(r-l)//2
                if row[mid] == target: return True
                elif row[mid] > target: r = mid - 1
                else: l = mid + 1
        return False
