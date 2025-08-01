# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return 0
        counts = Counter()

        def dfs(root):
            if not root: return 0

            curr = root.val + dfs(root.left) + dfs(root.right)
            counts[curr] += 1

            return curr
        
        dfs(root)

        try: 
            freq = counts.most_common(1)[0][1]
            return [key for key, value in counts.items() if value == freq]
        except:
            return []

            